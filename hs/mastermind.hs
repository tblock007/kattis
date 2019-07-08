import Data.List

main = interact (writeOutput . solve . readInput)

readInput :: String -> (String, String)
readInput s = (a,b)
    where 
        ss = tail $ words s
        a = head ss
        b = last ss

writeOutput :: (Int, Int) -> String
writeOutput (r,s) = show r ++ " " ++ show s

solve :: (String, String) -> (Int, Int)
solve (a,b) = (countMatches a b, countNonMatches a b)

countMatches :: String -> String -> Int
countMatches [] [] = 0
countMatches (a:as) (b:bs) = (if a == b then 1 else 0) + countMatches as bs

removeMatches :: String -> String -> (String, String)
removeMatches [] [] = ([], [])
removeMatches (a:as) (b:bs)
    | a == b = removeMatches as bs
    | otherwise = let (aa, bb) = removeMatches as bs in (a:aa, b:bb)

countNonMatches :: String -> String -> Int
countNonMatches a b = sumMins ca cb
    where 
        (aa, bb) = removeMatches a b
        ca = countOccur aa
        cb = countOccur bb
        
countOccur :: String -> [Int]
countOccur s = [length (filter (==c) s) | c <- ['A'..'Z']]

sumMins :: [Int] -> [Int] -> Int
sumMins [] [] = 0
sumMins (a:as) (b:bs) = (min a b) + sumMins as bs