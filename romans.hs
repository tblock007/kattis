main = interact (writeOutput . solve . readInput)

readInput :: String -> Float
readInput = read

writeOutput :: Int -> String
writeOutput = (++"\n") . show

solve :: Float -> Int
solve x = round (x * 1000 * 5280 / 4854)