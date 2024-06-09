// JavaScript code to make the image responsive
window.addEventListener('resize', function() {
    adjustImageSize();
});

function adjustImageSize() {
    var imageContainer = document.getElementById('image-container');
    var postImage = document.getElementById('post-image');

    // Calculate optimal width and height
    var containerWidth = imageContainer.offsetWidth;
    var containerHeight = imageContainer.offsetHeight;
    var imageWidth = postImage.naturalWidth;
    var imageHeight = postImage.naturalHeight;
    var widthRatio = containerWidth / imageWidth;
    var heightRatio = containerHeight / imageHeight;

    // Determine the appropriate scaling factor
    var scale = Math.min(widthRatio, heightRatio);

    // Set the image width and height based on the scaling factor
    postImage.style.width = (imageWidth * scale) + 'px';
    postImage.style.height = (imageHeight * scale) + 'px';
}

// Call the adjustImageSize function when the page loads
window.addEventListener('load', function() {
    adjustImageSize();
});
