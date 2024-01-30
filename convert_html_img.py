# This code example demonstrates how to convert HTML document to JPG images.
import aspose.words as aw

# Load an existing Word document
doc = aw.Document("Il_multithreading_01_new.html")

# Specify image save options
# Set save format as JPEG
imageOptions = aw.saving.ImageSaveOptions(aw.SaveFormat.JPEG)

# Set the "JpegQuality" property to "10" to use stronger compression when rendering the document.
# This will reduce the file size of the document, but the image will display more prominent compression artifacts.
imageOptions.jpeg_quality =20

# Change the horizontal resolution.
# The default value for these properties is 96.0, for a resolution of 96dpi.
# Similarly, change vertical resolution by setting vertical_resolution 
imageOptions.horizontal_resolution = 144

# Save the pages as JPG
for page in range(0, doc.page_count):
    extractedPage = doc.extract_pages(page, 1)
    extractedPage.save(f"C:\\Users\\informistica\\Dropbox\\Linguaggio_Python\\PythonThread\\img\\Page_{page + 1}.jpg", imageOptions)
   
   