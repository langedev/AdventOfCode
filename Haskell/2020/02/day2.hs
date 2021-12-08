
-- parseInput :: String -> (Int, Int, Char)
-- parseInput st = (ord (head st), read (tail (take 3 st)), tail (take 5 st))

parseMinimum :: String -> String -> Int
parseMinimum st out
  | h == '-' = read (reverse out)
  | h `elem` ['0'..'9'] = parseMinimum (tail st) (h:out)
  | otherwise = error "Unexpected input"
    where h = head st

parseMax :: String -> String -> Int
parseMax st out
  | h == ' ' = read (reverse out)
  | h == '-' = parseMax (tail st) ""
  | out == "!" = parseMax (tail st) "!"
  | h `elem` ['0'..'9'] = parseMax (tail st) (h:out)
  | otherwise = error "Unexpected input"
    where h = head st
