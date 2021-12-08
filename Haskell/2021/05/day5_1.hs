fand :: Bool -> Bool -> Bool
fand a b
  | a == b = True
  | otherwise = false

numberIntersections :: ((Integer, Integer), (Integer, Integer)) -> ((Integer, Integer), (Integer, Integer)) -> Int
numberIntersections ls1 ls2
  | fand (orien11 /= orien12) (orien21 /= orien22) = 1
  |
    where orien11 = orientation (fst ls1) (snd ls1) (fst ls2)
          orien12 = orientation (fst ls1) (snd ls1) (snd ls2)
          orien21 = orientation (fst ls2) (snd ls2) (fst ls1)
          orien22 = orientation (fst ls2) (snd ls2) (snd ls1)

onSegment :: (Integer, Integer) -> (Integer, Integer) -> (Integer, Integer) -> Int
onSegment p q r =

onSegmentFst :: Integer -> Integer -> Integer -> Bool
onSegmentFst p q r = fand (onSegmentLE (fst q) (fst p) (fst r)) (onSegmentGE (fst q) (fst p) (fst r))

onSegmentSnd :: Integer -> Integer -> Integer -> Bool
onSegmentSnd p q r = fand (onSegmentLE (snd q) (snd p) (snd r)) (onSegmentGE (snd q) (snd p) (snd r))

onSegmentGE :: Integer -> Integer -> Integer -> Bool
onSegmentGE a b c = a >= (min b c)

onSegmentLE :: Integer -> Integer -> Integer -> Bool
onSegmentLE a b c = a <= (max b c)

orientation :: (Integer, Integer) -> (Integer, Integer) -> (Integer, Integer) -> Int
orientation p q r
  | value == 0 = 0 -- Collinear
  | value > 0 = 1 -- Clockwise
  | otherwise = -1 -- CounterClockwise
    where value = ((snd q) - (snd p)) * ((fst r) - (fst q)) - ((fst q) - (fst p)) * ((snd r) - (snd q))


dummyInput = [((0,9),(5,9)),((8,0),(0,8)),((9,4),(3,4)),((2,2),(2,1)),((7,0),(7,4)),((6,4),(2,0)),((0,9),(2,9)),((3,4),(1,4)),((0,0),(8,8)),((5,5),(8,2))]
