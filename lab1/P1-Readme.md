# 5. Covert Sentence to Trees

## Short Sentence

En: $5,000 per person, the maximum allowed.

![image](https://user-images.githubusercontent.com/46303417/162590273-3bdbd0de-1c15-458a-bcf7-db826d337a8d.png)

Ch: 最高限額為每人5,000美元。

![image](https://user-images.githubusercontent.com/46303417/162590327-00d1b543-c2cd-42ad-acc2-60520406839f.png)

## Long Sentence

En: “We face a lot of competition, and we think transit can help,” said Joe Sternlieb, president of the Georgetown BID.

Tree1/2
![image](https://user-images.githubusercontent.com/46303417/162592432-1e5c53a8-3507-4aa3-a40d-7ab5f7b657b1.png)
Tree2/2
![image](https://user-images.githubusercontent.com/46303417/162592448-620d58b8-f08d-4199-8cf1-f3a3440543be.png)

Ch: ”我們面臨很多競爭，而我們認為政權轉移能對此局面有所幫助，”喬治城商業改善會主席喬·斯頓雷說道。

Tree 1/2
![image](https://user-images.githubusercontent.com/46303417/162592500-8926075b-d4bc-4cd9-8265-417c73eb4f0c.png)
Tree2/2
![image](https://user-images.githubusercontent.com/46303417/162592509-8d7d8e39-dd17-49a4-b5fb-e103902edbc6.png)

# 6. Alignments
If the alignemnts are done in word level, the sequence between English and Chinese is different. For example, the short sentence gives an illustration that English uses the inverted order to place propositional phrases as attributive at the end.

最高限額               為每人      5,000美元
the maximum allowed  per person  $5,000

Another one is that the main verd "said" is different and Chinese places it after the subject.

喬治城                商業改善會     主席          喬·斯頓雷       說道
the Georgetown (of)  BID          president     Joe Sternlieb said
