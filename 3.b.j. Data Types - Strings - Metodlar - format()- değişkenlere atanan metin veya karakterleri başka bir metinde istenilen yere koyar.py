# format()
# Bu metod stringleri biçimlendirmede kullanılır. Tanım olarak bu ama tam ifade-
# si, daha önceden hazırlanan değişkenleri metin içerisinde istenilen yerlere
# koyulmasını sağlar. Bu değişkenler aşağıda olduğu gibi kısa değişkenler de o-
# labilir uzun değişkenler de:

isim = "gökay"
soyisim = "özçoban"
print("Benim adım {}, soyadım {}".format.(isim,soyisim))
Benim adım gökay, soyadım özçoban

degisken1 ="""Bunu mümkün olduğunca uzun yazmayı düşünüyordum ama
ne yazacağımı da bilmediğimden böyle saçma sapan bi şekilde yazmaya başladım.
I wanted to write this sentence as long as possible but I didn't know what I'ıı
write about. That's why I drolled"""
degisken2 ="""Yukardaki degisken1'e benzer sözler falan filan..."""
print("""Yazı yazarken bazen şunu yazarım {}. Bazen de bunu yazmaya bile üşenir
şunu yazarım {}""".format(degisken1,degisken2))
Yazı yazarken bazen şunu yazarım: Bunu mümkün olduğunca uzun yazmayı düşünüyordum ama
ne yazacağımı da bilmediğimden böyle saçma sapan bi şekilde yazmaya başladım.
I wanted to write this sentence as long as possible but I didn't know what I'll
write about. That's why I drolled.
Bazen de bunu yazmaya bile üşenir şunu yazarım Yukardaki degisken1'e benzer sözler falan filan....

# format() metodunda parantezlerin içine yazılan değişkenlrin sıralaması önem-
# lidir. hangisinin ilk önce yazılması isteniyorsa parantezin içine ilk önce o
# yazılır.
