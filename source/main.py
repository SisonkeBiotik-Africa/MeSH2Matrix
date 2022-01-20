# Dataset Size: 46469
# Unique Labels: 195
# Dataset Shape: (46469, 89, 89)
# Labels Shape: (46469,)

import gdown
import numpy as np
import os

np.random.seed(1234)


def get_raw_dataset():
    url = 'https://drive.google.com/uc?id=1-IqQIFQ8X2wM0KU1qyIYZOvur8C_KdVh'
    output = '../output/dataset.txt'
    gdown.download(url, output)


def get_learning_dataset(is_downloaded=False):
    data_output = '../output/data.npy'
    labels_output = '../output/labels.npy'

    if is_downloaded is False:
        data_url = 'https://drive.google.com/uc?id=1-91tO2R6_TKBTYAe0o4DnRQGqbUcmoyk'
        labels_url = 'https://drive.google.com/uc?id=1hx1Li3u-R_EbpJttZtrcgBzkC9tX4aCj'

        gdown.download(data_url, data_output)
        gdown.download(labels_url, labels_output)

    data = np.load(data_output, allow_pickle=True)
    labels = np.load(labels_output, allow_pickle=True)

    train_frac = 0.8
    training_data, testing_data = data[:int(len(data) * train_frac)], data[int(len(data) * train_frac):]
    training_labels, testing_labels = labels[:int(len(labels) * train_frac)], labels[int(len(labels) * train_frac):]

    true_training_frac = 0.9

    real_training, dev_data = training_data[:int(len(training_data) * true_training_frac)], data[
                                                                                            int(len(
                                                                                                training_data) * true_training_frac):]

    real_training_labels, dev_labels = training_labels[:int(len(training_labels) * true_training_frac)], labels[int(
        len(training_labels) * true_training_frac):]

    print('Train Size: {} with shape: {}'.format(len(real_training), real_training.shape))
    print('Dev Size: {} with shape: {}'.format(len(dev_data), dev_data.shape))
    print('Test Size: {} with shape: {}'.format(len(testing_data), testing_data.shape))

    return (real_training, real_training_labels), (dev_data, dev_labels), (testing_data, testing_labels)


def get_grouped_labels():
    train_group_out = '../output/grouped_train_labels.npy'
    dev_group_out = '../output/grouped_dev_labels.npy'
    test_group_out = '../output/grouped_test_labels.npy'

    train_ = 'https://drive.google.com/uc?id=1lWsvwDWQ_syd2bWgnkyWze6BjzVvWe57'
    dev_ = 'https://drive.google.com/uc?id=17VAlNtL4hHcBH3Ibs2emzxnBTbdxoM0O'
    test_ = 'https://drive.google.com/uc?id=1kmuf84Le-vER4IolgJCfZPy-1J-NSNtr'

    if (not os.path.exists(train_group_out)) and (not os.path.exists(dev_group_out)) and (
            not os.path.exists(test_group_out)):
        print('Downloading Grouped Labels to ../output/')
        gdown.download(train_, train_group_out)
        gdown.download(dev_, dev_group_out)
        gdown.download(test_, test_group_out)


def main():
    save = False

    data_file = '../output/data.npy'
    labels_file = '../output/labels.npy'

    if os.path.exists(data_file) and os.path.exists(labels_file):
        print('Data and Labels files found. Loading from local disk')
        train, dev, test = get_learning_dataset(is_downloaded=True)
    else:
        save = True
        train, dev, test = get_learning_dataset()
        get_grouped_labels()

    train_set_data, train_set_label = train[0], train[1]
    dev_set_data, dev_set_label = dev[0], dev[1]
    test_set_data, test_set_label = test[0], test[1]

    if save:
        # Save the train, test and dev numpy files
        print('Saving Files ...')
        np.save('../output/train.npy', train_set_data, allow_pickle=True)
        np.save('../output/train_labels.npy', train_set_label, allow_pickle=True)
        np.save('../output/dev.npy', dev_set_data, allow_pickle=True)
        np.save('../output/dev_labels.npy', dev_set_label, allow_pickle=True)
        np.save('../output/test.npy', test_set_data, allow_pickle=True)
        np.save('../output/test_labels.npy', test_set_label, allow_pickle=True)
        print('All Files Saved Successfully!')


if __name__ == '__main__':
    main()
