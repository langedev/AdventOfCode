fishGrowth :: [Integer] -> [Integer]
fishGrowth [] = []
fishGrowth (x:xs)
  | x == 0 = 6 : 8 : fishGrowth xs
  | otherwise = (x-1) : fishGrowth xs

runFishGrowth :: [Integer] -> Int -> [Integer]
runFishGrowth ls 0 = ls
runFishGrowth ls x = runFishGrowth (fishGrowth ls) (x-1)

fishGrowth' :: [(Int, Integer)] -> Int -> Int -> [(Int, Integer)]
fishGrowth' [] new _ = (8,x) : []
fishGrowth' (stage,num):xs new reset
  | stage == 0 = fishGrowth' xs new num
  | stage == 7 = (6, num + reset) : fishGrowth' xs new 0
  | otherwise = ((stage-1), num) : fishGrowth' xs new 0

input = [1,2,1,3,2,1,1,5,1,4,1,2,1,4,3,3,5,1,1,3,5,3,4,5,5,4,3,1,1,4,3,1,5,2,5,2,4,1,1,1,1,1,1,1,4,1,4,4,4,1,4,4,1,4,2,1,1,1,1,3,5,4,3,3,5,4,1,3,1,1,2,1,1,1,4,1,2,5,2,3,1,1,1,2,1,5,1,1,1,4,4,4,1,5,1,2,3,2,2,2,1,1,4,3,1,4,4,2,1,1,5,1,1,1,3,1,2,1,1,1,1,4,5,5,2,3,4,2,1,1,1,2,1,1,5,5,3,5,4,3,1,3,1,1,5,1,1,4,2,1,3,1,1,4,3,1,5,1,1,3,4,2,2,1,1,2,1,1,2,1,3,2,3,1,4,5,1,1,4,3,3,1,1,2,2,1,5,2,1,3,4,5,4,5,5,4,3,1,5,1,1,1,4,4,3,2,5,2,1,4,3,5,1,3,5,1,3,3,1,1,1,2,5,3,1,1,3,1,1,1,2,1,5,1,5,1,3,1,1,5,4,3,3,2,2,1,1,3,4,1,1,1,1,4,1,3,1,5,1,1,3,1,1,1,1,2,2,4,4,4,1,2,5,5,2,2,4,1,1,4,2,1,1,5,1,5,3,5,4,5,3,1,1,1,2,3,1,2,1,1]
