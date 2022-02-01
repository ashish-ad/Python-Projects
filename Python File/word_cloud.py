from wordcloud import WordCloud
import wikipedia
import matplotlib.pyplot as plt 
text = wikipedia.summary("node js")
#print(text.split())
w = WordCloud(background_color = "Blue")
w.generate(text)
plt.imshow(w)
plt.axis("off")
plt.show()
plt.savefig('w.jpg',dpi=1080)
