import gdown
import os


def download_weights(model_name, url, num_class):
    output_dir = 'pretrained_{}_weights'.format(model_name.upper())
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    output = output_dir + '/{}_{}_pretrained'.format(model_name, num_class)
    info = 'Downloading pretrained weights of {} model with {} classes ---> {}'.format(model_name.upper(), num_class,
                                                                                       output)
    print(info)
    gdown.download(url, output)


if __name__ == '__main__':
    fc_195_link = 'https://drive.google.com/uc?id=1-lWUFD3wxuWEtiR1H-MQtKlJh6MF6hia'
    fc_5_link = 'https://drive.google.com/uc?id=1-3nQkgAtznQYHYOpwcxf9IUFhDX4YxmQ'

    download_weights('fc', fc_195_link, 195)
    download_weights('fc', fc_5_link, 5)
