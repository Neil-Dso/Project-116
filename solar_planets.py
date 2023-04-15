import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "Sun",
    (20,300),
    cv2.QT_FONT_BLACK,
    1.5,
    (255,255,255)
)

cv2.putText(
    img,
    "Mercury",
    (90,150),
    cv2.QT_FONT_BLACK,
    1,
    (128,128,128)
)

cv2.putText(
    img,
    "Venus",
    (170,300),
    cv2.QT_FONT_BLACK,
    1,
    (0,165,255)
)

cv2.putText(
    img,
    "Earth",
    (270,150),
    cv2.QT_FONT_BLACK,
    1,
    (0,255,0)
)

cv2.putText(
    img,
    "Mars",
    (370,300),
    cv2.QT_FONT_BLACK,
    1,
    (0,0,255)
)

cv2.putText(
    img,
    "Jupiter",
    (520,150),
    cv2.QT_FONT_BLACK,
    1,
    (30,20,40)
)

cv2.putText(
    img,
    "Saturn",
    (750,300),
    cv2.QT_FONT_BLACK,
    1,
    (88, 133, 152)
)

cv2.putText(
    img,
    "Uranus",
    (950,150),
    cv2.QT_FONT_BLACK,
    1,
    (255,180,180)
)

cv2.putText(
    img,
    "Neptune",
    (1100,300),
    cv2.QT_FONT_BLACK,
    1,
    (255,0,0)
)

cv2.imwrite("solar-system-with-names.jpg", img)
cv2.imshow("solar-system.jpg", img)
cv2.waitKey(0)