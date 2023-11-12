import os
import pandas as pd
from PIL import Image, ImageOps
import torch
from torch.utils.data import Dataset
from torchvision.transforms import ToTensor



class WaldoDataset(Dataset):
    def __init__(self, metadata_file, root, dimensions=None):
        self.metadata = pd.read_csv(metadata_file)
        self.root = root
        self.dims = dimensions
        self.transform = ToTensor()


    def __len__(self):
        return len(self.metadata)


    def __getitem__(self, idx):
        img_data = self.metadata.iloc[idx]
        img_path = os.path.join(self.root, img_data['path'])
        img_dims = (img_data['width'], img_data['height'])
        img_label = img_data['label']

        img = Image.open(img_path)

        if self.dims and self.dims != img_dims:
            img = ImageOps.fit(img, self.dims, Image.ANTIALIAS)

        return self.transform(img), img_label



if __name__ == '__main__':
    import matplotlib.pyplot as plt


    waldo_data = WaldoDataset('waldo_metadata.csv', '../data')
    sample_idx = torch.randint(len(waldo_data), size=(1,)).item()
    img, label = waldo_data[sample_idx]

    fig, ax = plt.subplots(figsize=(4, 4))
    plt.title(("Not " if label == 0 else "") + "Waldo", fontsize=16)
    plt.axis('off')
    plt.imshow(img.permute(1, 2, 0))
    plt.show()
