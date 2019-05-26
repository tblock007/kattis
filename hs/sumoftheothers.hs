import Data.List

main = interact (writeOutput . solve . readInput)

readInput :: String -> [[Int]]
readInput = (map convert) . (map words) . lines
    where 
        convert :: [String] -> [Int]
        convert ss = [read s | s <- ss]

writeOutput :: [Int] -> String
writeOutput = unlines . (map show)

solve :: [[Int]] -> [Int]
solve ls = map solveInstance ls

solveInstance :: [Int] -> Int
solveInstance l = (sum l) `quot` 2