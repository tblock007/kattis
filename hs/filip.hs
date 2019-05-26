import Data.List

main = interact (writeOutput . solve . readInput)

readInput :: String -> [String]
readInput = words

writeOutput :: Int -> String
writeOutput = show

solve :: [String] -> Int
solve (x:y:[]) = if rx > ry then rx else ry
    where         
        rx = read (reverse x)
        ry = read (reverse y)