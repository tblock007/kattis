main = interact (writeOutput . solve . readInput)

readInput :: String -> [[Int]]
readInput s = map threeInts (actualLines s)
    where 
        actualLines :: String -> [String]
        actualLines = tail . lines

        threeInts :: String -> [Int]
        threeInts = (map read) . words

writeOutput :: [String] -> String
writeOutput = unlines

solve :: [[Int]] -> [String]
solve [] = []
solve (x:xs) = (assess x):(solve xs)
    where 
        assess :: [Int] -> String
        assess (r:e:c:[]) 
            | e - c > r = "advertise"
            | e - c == r = "does not matter"
            | otherwise = "do not advertise"
