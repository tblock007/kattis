import Data.List

main = interact (writeOutput . solve . readInput)

readInput :: String -> [(String, [Int])]
readInput text = parse (tail (lines text))

parse :: [String] -> [(String, [Int])]
parse [] = []
parse (p:_:l:ls) = (p, read l) : (parse ls)

writeOutput :: [String] -> String
writeOutput = unlines

solve :: [(String, [Int])] -> [String]
solve l = map solveInstance l

solveInstance :: (String, [Int]) -> String
solveInstance (p, l) = let (ah, at, r) = countDrops p in modList l (ah,at) r

modList :: [Int] -> (Int, Int) -> Bool -> String
modList l (h,t) r
    | h + t > size = "error"
    | r = show (reverse cut)
    | otherwise = show cut
    where 
        size = length l
        cut = take (size - h - t) (drop h l)

countDrops :: String -> (Int, Int, Bool)
countDrops p = countDropsAcc p (0, 0, False)

countDropsAcc :: String -> (Int, Int, Bool) -> (Int, Int, Bool)
countDropsAcc [] (ah, at, r) = (ah, at, r)
countDropsAcc (c:cs) (ah, at, r)
    | c == 'R' = countDropsAcc cs (ah, at, not r)
    | c == 'D' && r = countDropsAcc cs (ah, at + 1, r)
    | otherwise = countDropsAcc cs (ah + 1, at, r)
