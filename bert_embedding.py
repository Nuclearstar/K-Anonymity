import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

module_url = "https://tfhub.dev/google/universal-sentence-encoder/1?tf-hub-format=compressed"

# Import the Universal Sentence Encoder's TF Hub module
embed = hub.Module(module_url)

# sample text
condition_list = \
    ['subchronic catatonic schizophrenia',
     'end stage renal disease',
     'Toxic multinodular goiter',
     'Chronic pain due to injury',
     'Arthralgia of the lower leg']


# df = pd.read_csv("./data/finalConditionInfo.csv", sep=",", index_col=False, engine='python');
#
# condition_list_ori = df['condition'].unique().tolist()
#
# condition_list = [str.lower(condition.replace('-', ' ')) for condition in condition_list_ori]

def plot_similarity(labels, features, rotation):
  corr = np.inner(features, features)
  sns.set(font_scale=1.2)
  g = sns.heatmap(
      corr,
      xticklabels=labels,
      yticklabels=labels,
      vmin=0,
      vmax=1,
      cmap="YlOrRd")
  g.set_xticklabels(labels, rotation=rotation)
  g.set_title("Semantic Textual Similarity")


def run_and_plot(session_, input_tensor_, messages_, encoding_tensor):
  message_embeddings_ = session_.run(
      encoding_tensor, feed_dict={input_tensor_: messages_})
  plot_similarity(messages_, message_embeddings_, 90)

def heatmap(x_labels, y_labels, values):


    fig, ax = plt.subplots()
    im = ax.imshow(values)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(x_labels)))
    ax.set_yticks(np.arange(len(y_labels)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(x_labels)
    ax.set_yticklabels(y_labels)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(y_labels)):
        for j in range(len(x_labels)):

            text = ax.text(j, i, "%.2f" % values[i, j], ha="center", va="center", color="w")

    fig.tight_layout()

    plt.show()


similarity_input_placeholder = tf.placeholder(tf.string, shape=(None))
similarity_message_encodings = embed(similarity_input_placeholder)

with tf.Session() as session:

    session.run(tf.global_variables_initializer())
    session.run(tf.tables_initializer())

    run_and_plot(session, similarity_input_placeholder, condition_list, similarity_message_encodings)

    message_embeddings_ = session.run(similarity_message_encodings, feed_dict={similarity_input_placeholder: condition_list})

    corr = np.inner(message_embeddings_, message_embeddings_)

    print(corr)
    print(condition_list)

    heatmap(condition_list, condition_list, corr)


