main = interact (writeOutput . solve . readInput)

readInput :: String -> [Int]
readInput s = map read (tail (lines s))

writeOutput :: [String] -> String
writeOutput = unlines

solve :: [Int] -> [String]
solve [] = []
solve (x:xs) = (assess x):(solve xs)
    where 
        assess :: Int -> String
        assess x
            | x == 0 = "1"
            | x == 1 = "1"
            | x == 2 = "2"
            | x == 3 = "6"
            | x == 4 = "4"
            | otherwise = "0"
