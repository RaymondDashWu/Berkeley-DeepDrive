# Berkeley DeepDrive Image Segmentation Attempt
## Work in Progress

This was my attempt to create an image segmentation model using Berkeley's DeepDrive dataset. A more complete writeup documenting the journey can be found in my medium post.
https://medium.com/p/308f8c44305a/edit

The original dataset can be downloaded here:
https://bdd-data.berkeley.edu/

### Installation

To recreate my results you'll need your Linux distro of choice, PyTorch v1 and Python 3.6 or later.

```sh
$ conda install -c pytorch -c fastai fastai
```
From there Berkeley DeepDrive v2.ipynb should run. v1 was created using an earlier version of FastAI and did not successfully segment.


### Included
label_quantify.py
* Was used to determine how many categories there were. Companion to test_label_quantify.json

seg_128 folder
* A 128x128 bordered version of the segmentation dataset used to train ResNet34. Could be used as a quick reference to try deeper ResNet or other pretrained models.

### Task list
- [X] Implement U-Net
- [ ] Implement 100-layer Tiramisu
- [ ] Mask R-CNN
  - Note: Explored but no implementation attempted