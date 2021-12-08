fand :: Bool -> Bool -> Bool
fand a b
  | a == b = a
  | otherwise = False

betweenxAndy :: Int -> Int -> Int -> Bool
betweenxAndy x y n = fand (n >= x) (n <= y)

between0And1 :: Int -> Bool
between0And1 = betweenxAndy 0 1

crossProduct :: (Integer, Integer) -> (Integer, Integer) -> Integer
crossProduct (x1, y1) (x2, y2) = x1*y2 - x2*y1

dotProduct :: (Integer, Integer) -> (Integer, Integer) -> Integer
dotProduct (x1, y1) (x2, y2) = x1*x2 + y1*y2

pointDifference :: (Integer, Integer) -> (Integer, Integer) -> (Integer, Integer)
pointDifference (x1, y1) (x2, y2) = (x1-x2, y1-y2)

pointSum :: (Integer, Integer) -> (Integer, Integer) -> (Integer, Integer)
pointSum (x1, y1) (x2, y2) = (x1+x2, y1+y2)

overlapNums :: ((Integer,Integer),(Integer,Integer)) -> ((Integer,Integer),(Integer,Integer)) -> Int
overlapNums (p, r) (q, s)
  | collinear =
  | paraNonInter = 0
  | intersect = 1
  | otherwise = 0
    where bottom = crossProduct r s
          tTop = crossProduct (pointDifference q p) s
          top = crossProduct (pointDifference q p) r
          collinear = fand (bottom == 0) (top == 0)
          paraNonInter = fand (bottom == 0) (top /= 0)
          u = top / bottom
          t = tTop / bottom
          intersect = fand (bottom /= 0) (fand (between0And1 u) (between0And1 t))

collineComp :: ((Integer,Integer),(Integer,Integer)) -> ((Integer,Integer),(Integer,Integer)) -> Int
collineComp (p, r) (q, s)
  | fand (t0' < 0) (t1 >= 0) = 0-- overlapping
  | fand (t0' >= 0) (t1 <= 1) = 0-- overlapping
  | otherwise = 0 -- Disjoint
    where t0 = (dotProduct (pointDifference p q) r) / dotProduct r r
          t1 = (dotProduct (pointDifference (pointSum q s) p) r) / dotProduct r r
          t0' = if t0 > t1 then t1 else t0
          t1' = if t0 > t1 then t0 else t1

collineComp :: ((Integer,Integer),(Integer,Integer)) -> ((Integer,Integer),(Integer,Integer)) -> Int
