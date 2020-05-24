# Image Stitching for Panorama Generation
You've found a homography-based image stitching application to create panoramas packaged into a Django web app. It uses SIFT, SURF or ORB features (your choice, but there isn't much of a difference) to find homographies, warp corresponding images and stitch them by overlaying them appropriately. It only implements planar warping as of now - hopefully I'll be able to add functionality for cylindrical warping in the future.

If you're only interested in the image stitching code, check out ``stitch/imagestitching.py``. It's a bit sparse on documentation right now - I'll expand on it when time permits. If something doesn't make sense or if you have any suggestions, feel free to contact me on sha.gpt4@gmail.com.
