def designerPdfViewer(h, word):
    maxi=0
    for i in range(len(word)):
        if(maxi< h[ord(word[i])-97]):
            maxi = h[ord(word[i])-97]
    return maxi*len(word)


h = [1,2,3,4,5]
word = "aza"
print(designerPdfViewer(h,word))



