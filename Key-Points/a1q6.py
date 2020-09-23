import cv2
import numpy as np

def calc_cdf(hist,L):
    cdf = np.copy(hist)
    n_hist = np.sum(hist)
    cdf = hist/n_hist
    for i in range(1,L):
        cdf[i] = cdf[i] + cdf[i-1]
    return cdf

def calc_lut(cdf1,cdf2,L):
    lutab = np.zeros(L)
    luval = 0
    for pxval1 in range(L):
        luval
        for pxval2 in range(L):
            if cdf2[pxval2] >= cdf1[pxval1]:
                luval = pxval2
                break
        lutab[pxval1] = luval
    return lutab

def histEqualization(im):
    img = np.array(im)
    height,width = img.shape[:2]
    N = height * width
    img = linContrastStretching(img,0,255)
    
    #Array for new_image
    he_img = np.zeros(img.shape)
    L = 256
    intsc, intsv = np.histogram(img.flatten(),L,[0,L-1])
    #print(intsc)
    #print(intsv)
    #print(intsv.shape)
    #Calculate CDF
    cdf = calc_cdf(intsc,L)
    cdf = np.floor(cdf*(L-1)).astype('uint8')
    plt.plot(range(0,L),cdf)
    plt.show()
    
    for y in range(0, height):
        for x in range(0, width): #Apply the new intensities in our new image
            he_img[y,x] = np.floor(cdf[img[y,x]]).astype('uint8')
    
    print(he_img)
    
    #PLOT THE HISTOGRAMS
    plt.hist(img.ravel(),L,[0,L-1])
    plt.xlabel('Intensity Values')
    plt.ylabel('Pixel Count')
    plt.show()
    
    plt.hist(he_img.ravel(),L,[0,L-1])
    plt.xlabel('Intensity Values')
    plt.ylabel('Pixel Count')
    plt.show()
    
    return he_img

def histMatching(src_image, ref_image):
    src = np.copy(src_image)
    ref = np.copy(ref_image)

    src_hist, src_bin = np.histogram(src.flatten(), 256, [0,256])
    ref_hist, ref_bin = np.histogram(ref.flatten(), 256, [0,256])

    src_cdf = calc_cdf(src_hist,256)
    ref_cdf = calc_cdf(ref_hist,256)

    lookup_table = calc_lut(src_cdf, ref_cdf, 256)

    img_after_transform = cv2.LUT(src, lookup_table)

    image_after_matching = cv2.convertScaleAbs(img_after_transform)

    fig2 = plt.figure(figsize=(32,32))
    ax4 = fig2.add_subplot(1,1,1)
    ax4.imshow(image_after_matching, cmap='gray')
    ax4.axis('off')

    return image_after_matching


