countIncreases :: [Integer] -> Integer
countIncreases [_] = 0
countIncreases x
  | previous < current = 1 + countIncreases (tail x)
  | otherwise = countIncreases (tail x)
    where previous = head x
          current = head (tail x)

--data1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

window :: [Integer] -> [Integer]
window [] = []
window [_] = []
window [_,_] = []
window st = (a+b+c):window (tail st)
  where a = head st
        b = head (tail st)
        c = head (tail (tail st))
