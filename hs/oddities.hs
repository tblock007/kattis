main = interact (writeOutput . solve . readInput)

readInput :: String -> [Int]
readInput = (map read) . tail . lines

writeOutput :: [String] -> String
writeOutput = unlines

solve :: [Int] -> [String]
solve [] = []
solve (x:xs) = (fs x) : (solve xs)
    where 
        fs :: Int -> String
        fs x
            | even x = (show x) ++ " is even"
            | otherwise = (show x) ++ " is odd"
