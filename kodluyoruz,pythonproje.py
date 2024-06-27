#iki nokta arası oklid mesafesi hesaplama 

import math 

points = [(1,2),(3,4),(5,6)]

def euclideanDistance(point1,point2):
        (x1, y1) = point1
        (x2, y2) = point2
        distances = math.sqrt((x2-x1)**2 + (y2-y1)**2)   #karekök almak için .sqrt
        return distances


distances = [euclideanDistance(points[a],points[b])   #listComprehensionsS
             for a in range(len(points))
             for b in range(a+1, len(points))]



enKisaMesafe = min(distances)

print(f"minimum öklid mesafesi {enKisaMesafe}'dir.")