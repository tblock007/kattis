import Data.List

main = interact (writeOutput . solve . readInput)

readInput :: String -> ([Int], [[Int]])
readInput s = (parseInit (head ls), parseQueries (tail ls))
    where 
        ls = tail (lines s)

parseInit :: String -> [Int]
parseInit = (map read) . words

parseQueries :: [String] -> [[Int]]
parseQueries = map pq
    where 
        pq :: String -> [Int]
        pq = (map read) . words

writeOutput :: [Int] -> String
writeOutput = unlines . (map show)

solve :: ([Int], [[Int]]) -> [Int]
solve = uncurry solveAux

solveAux :: [Int] -> [[Int]] -> [Int]
solveAux _ [] = []
solveAux c ((q@(com:a:b:[])):qs)
    | com == 1 = solveAux ((take (a - 1) c) ++ [b] ++ (drop a c)) qs
    | com == 2 = (query (c !! (a - 1)) (c !! (b - 1))) : (solveAux c qs)

query :: Int -> Int -> Int
query a b = abs (a - b)