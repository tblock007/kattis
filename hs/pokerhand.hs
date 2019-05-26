import Data.List

main = interact (writeOutput . solve . readInput)

readInput :: String -> [Char]
readInput l = [head w | w <- words l]

writeOutput :: Int -> String
writeOutput = (++"\n") . show

solve :: [Char] -> Int
solve = maximum . (map length) . group . sort