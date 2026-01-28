import os
import sys
import json

# Ensure src is in path
sys.path.append(os.getcwd())

try:
    from src.pipeline import PharmaPipeline
except ImportError as e:
    print(f"Error importing PharmaPipeline: {e}")
    sys.exit(1)

def verify():
    print("Initializing PharmaPipeline...")
    try:
        pipeline = PharmaPipeline()
        print("Pipeline initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize pipeline: {e}")
        return

    # Check for a test image
    image_path = os.path.join("data", "test_upload.jpg")
    if not os.path.exists(image_path):
        print(f"Warning: {image_path} not found. Checking for other images...")
        # Fallback: try to find any jpg
        import glob
        jpgs = glob.glob("*.jpg")
        if jpgs:
            image_path = jpgs[0]
            print(f"Using found image: {image_path}")
        else:
            print("No test images found. Skipping processing test.")
            return

    print(f"Processing image: {image_path}")
    try:
        result = pipeline.process_image(image_path)
        print("Processing complete.")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error during processing: {e}")

if __name__ == "__main__":
    verify()
