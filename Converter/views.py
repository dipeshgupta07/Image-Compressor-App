from django.shortcuts import render, HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans
import imageio.v2 as imageio
import io
import base64

# Home page with image upload form
def index(request):
    return render(request, 'index.html')

# Process the uploaded image and compress it using KMeans
def process(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')
        if not uploaded_file:
            return HttpResponse("No image uploaded.")

        # Save the image temporarily
        file_path = default_storage.save(f'temp/{uploaded_file.name}', ContentFile(uploaded_file.read()))
        full_path = default_storage.path(file_path)

        try:
            # Load and normalize image
            image = imageio.imread(full_path)
            image = image / 255.0  # Normalize pixel values to 0–1

            img_shape = image.shape
            if len(img_shape) != 3 or img_shape[2] not in [3, 4]:
                return HttpResponse("Only RGB or RGBA images are supported.")

            channels = img_shape[2]
            X = image.reshape(-1, channels)

            # KMeans Compression
            K = 8  # Number of color clusters
            kmeans = MiniBatchKMeans(n_clusters=K, random_state=0)
            kmeans.fit(X)

            centroids = kmeans.cluster_centers_
            labels = kmeans.labels_
            X_compressed = centroids[labels]
            compressed_image = X_compressed.reshape(img_shape)

            # Save compressed image to memory
            buffer = io.BytesIO()
            plt.imsave(buffer, compressed_image, format='png')
            buffer.seek(0)

            image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
            request.session['compressed_image'] = image_base64  # Save to session for download

            return render(request, 'com.html', {
                'image_base64': image_base64,
                'shape': img_shape,
                'channels': channels,
            })

        except Exception as e:
            return HttpResponse(f"Error processing image: {str(e)}")

    return render(request, 'index.html')

# Allow user to download the compressed image
def download_image(request):
    image_base64 = request.session.get('compressed_image')
    if not image_base64:
        return HttpResponse("No image available", status=404)

    image_bytes = base64.b64decode(image_base64)
    buffer = io.BytesIO(image_bytes)

    response = HttpResponse(buffer.getvalue(), content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="compressed_image.png"'
    return response
