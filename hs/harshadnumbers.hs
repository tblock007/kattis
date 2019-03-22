main = interact (writeOutput . solve . readInput)

readInput :: String -> Int
readInput = read

writeOutput :: Int -> String
writeOutput = (++"\n") . show

solve :: Int -> Int
solve n 
    | isHarshad n = n
    | otherwise = (solve (n + 1))

isHarshad :: Int -> Bool
isHarshad n 
    | mod n (digitSum n) == 0 = True
    | otherwise = False

digitSum :: Int -> Int
digitSum n
    | n < 10 = n
    | otherwise = (n `mod` 10) + (digitSum (n `quot` 10))

