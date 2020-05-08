from PIL import Image
import imagehash
import azure.functions  
  
  


def main(req: azure.functions.HttpRequest) -> str:
    #user = req.params.get('user')
    hash0 = imagehash.average_hash(Image.open('test.jpg')) 
    hash1 = imagehash.average_hash(Image.open('testing1.jpg')) 
    cutoff = 5
    if hash0 - hash1 < cutoff:
        return 'images are similar'
    else:
        return 'images are not similar'
    