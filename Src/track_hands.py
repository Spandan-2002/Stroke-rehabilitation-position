# -*- coding: utf-8 -*-
"""Track_hands.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13ZEVpBrt6vQ7RF7W8t33508Jqsaf5LMR
"""

def track_hands_with_sam2(video_path, output_path):
    """ Track hands using bounding box. """
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    frame_num = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        hand_boxes = detect_hands_in_frame(frame)
        masks = []

        for (x_min, y_min, x_max, y_max) in hand_boxes:
            mask = np.zeros((frame_height, frame_width), dtype=np.uint8)
            mask[y_min:y_max, x_min:x_max] = 255
            mask = np.stack([mask] * 3, axis=-1)
            masks.append(mask)

        alpha = 0.5
        masked_frame = frame.copy()
        for mask in masks:
            masked_frame[mask[:, :, 0] > 0] = (
                masked_frame[mask[:, :, 0] > 0] * (1 - alpha) + np.array([0, 255, 0]) * alpha
            ).astype(np.uint8)

        out.write(masked_frame)
        frame_num += 1

    cap.release()
    out.release()
    print(f"Processed video saved to {output_path}")