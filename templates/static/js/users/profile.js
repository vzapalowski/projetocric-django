function previewImage(event) {
    const previewImage = document.getElementById('image-preview');
    const file = event.target.files[0];
    
    if (file) {
      previewImage.src = URL.createObjectURL(file);
      document.body.style.overflow = 'hidden';
      document.getElementById('image-preview-container').style.display = 'flex';
    }
  }

function cancelPreview() {
    document.body.style.overflow = 'auto';
    document.getElementById('image-preview-container').style.display = 'none';
    document.getElementById('image-preview').src = '';
    window.location.reload();
}

function savePreview() {
    const previewImage = document.getElementById('image-preview');
    if (previewImage.src) {
      const formData = new FormData();
      formData.append('user_id', userId); 
      formData.append('image', document.querySelector('#file-upload').files[0]);

      fetch(uploadUrl, {
        method: 'POST',
        body: formData,
      })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        cancelPreview();
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }
}
