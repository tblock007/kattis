main = interact (writeOutput . solve . readInput)

readInput :: String -> [[Float]]
readInput s = map read2float (tail (lines s))
    where
        read2float :: String -> [Float]
        read2float l = map read (words l) 

writeOutput :: Float -> String
writeOutput f = (show f) ++ "\n"

solve :: [[Float]] -> Float
solve [] = 0.0
solve (x@(q:y:[]):xs) = (q * y) + (solve xs)
