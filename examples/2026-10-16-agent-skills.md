---
title: Ajan skill'leri — ne oldukları, nasıl yazıldıkları, nasıl paylaşıldıkları
date: 2026-10-16
decision: literature-review skill'ini GitHub'da ve LinkedIn'de nasıl sunacağız; hangi iddiaları dürüstçe yapabiliriz
confidence: medium
---

# Ajan skill'leri: ne oldukları, nasıl yazıldıkları, nasıl paylaşıldıkları

## Çerçeve

**Karar.** Yazdığımız `literature-review` skill'ini başkalarının benimseyeceği
biçimde nasıl yazar, paketler ve anlatırız; tanıtırken hangi iddiaları
kaynak göstererek yapabiliriz.

**Bağlam.** Skill bir Claude Code kullanıcısı tarafından kişisel dizinde
yazıldı (`~/.claude/skills/literature-review/`), tek bir `SKILL.md` ve bir
rapor şablonundan oluşuyor. Hedef: GitHub'da herkese açık bir depo ve
LinkedIn'de Türkçe bir gönderi. Okuyucu kitlesi yazılımcılar; çoğu skill
kavramını yeni duyuyor. Bu bağlam konuşmadan çıkarıldı; yanlışsa düzeltilir.

**Alt sorular.**

1. Ajan skill'i biçimsel olarak nedir, hangi araçlar bu biçimi destekliyor?
2. Skill yazmanın en iyi pratikleri neler, kim söylüyor, hangisi ölçüme dayanıyor?
3. Skill'ler fiilen nasıl dağıtılıyor ve kuruluyor; popüler skill depolarının ortak yanı ne?
4. LLM'lerin literatür taraması yapması üzerine araştırma ne diyor: hata biçimleri ve neyin azalttığı?

## Özet

Skill biçimi gerçek ve yerleşmiş: Anthropic'in Ekim 2025'te çıkardığı,
Aralık 2025'te açık standart yaptığı `SKILL.md` klasörünü bugün Codex,
Cursor, Gemini CLI, GitHub Copilot ve VS Code dahil kırka yakın araç okuyor
[S1][S2][S9]. Dağıtım için fiilî yol herkese açık bir GitHub deposu; Claude
Code tarafında depoya tek bir `marketplace.json` eklemek onu eklenti yapar,
diğer ajanlar için `npx skills add owner/repo` çalışır [S21][S27].

Yazım pratiklerinde uzlaşma var ama ölçüm az: "açıklama tek tetikleyicidir,
gövde kısa olsun, ayrıntı yan dosyaya" cümlesi hem spesifikasyonda hem
üreticide hem uygulayıcılarda aynı [S1][S5][S31]. Buna karşılık 2026'da
çıkan üç ölçüm skill'lerin ortalama etkisinin küçük olduğunu, kazancın
içeriğin işe uyup uymadığına bağlı olduğunu gösteriyor: 49 kamusal skill'in
39'u görev başarısını hiç değiştirmemiş [S35]. Anthropic'in kendi iki
belgesi "açıklama iddialı olsun" ile "yeni modellerde iddialı dili geri
çek" arasında çelişiyor [S31][S33].

Skill'imizin tasarımı için en önemli bulgu dördüncü alt sorudan geliyor:
LLM'ler bellekten yazdıklarında atıfların %18–55'ini uyduruyor [S41]; web'e
bağlıyken bu %3–13'e düşüyor ama bitmiyor [S44]; bağlantı doğrulama aracı
verilip düzeltme istendiğinde %16'dan %0,6'ya iniyor [S44]. Çalışan bir
bağlantı iddiayı desteklediği anlamına gelmiyor: sınır modellerde bağlantı
%94–100 çalışıyor, iddiayı yalnızca %39–77'si destekliyor [S47]. Varsayılan
çıktı tek taraflı: tartışmalı sorularda cevapların %52–95'i tek tarafı
anlatıyor [S48]. Skill'in "her kaynağı getir, iddia kartı yaz, uzlaşma ve
anlaşmazlığı ayır" tasarımı bu üç bulguyla örtüşüyor; eksik olan,
doğrulamanın bir talimat değil bir mekanizma olması.

**Öneri:** depoyu açık standartla uyumlu, betiksiz ve harici çağrısız
tut (en küçük güven yarıçapı), skill'e bağlantı doğrulama adımı ve tur
başına kaynak tavanı ekle, tanıtımda "kaynaklı" demek yerine üç ayrı
ölçüyü söyle: bağlantı çalışıyor mu, konuyla ilgili mi, iddiayı destekliyor
mu. Güven: **orta**.

## Bulgular

### 1 · Skill biçimsel olarak nedir, kim destekliyor?

**Uzlaşma.** Skill, içinde en az bir `SKILL.md` bulunan bir klasördür.
Dosya YAML ön bölüm artı Markdown gövdedir; zorunlu alan yalnızca `name`
(1–64 karakter, küçük harf, klasör adıyla aynı) ve `description`
(1–1024 karakter). İsteğe bağlı `license`, `compatibility`, `metadata`,
`allowed-tools`; alışılmış alt klasörler `scripts/`, `references/`,
`assets/` [S1]. Yükleme üç katmanlıdır: her skill'in ad ve açıklaması her
oturumda bağlamdadır (skill başına yaklaşık 100 token), gövde yalnızca
model skill'i seçince yüklenir (5.000 token altı önerilir), yan dosyalar
ancak gövde onlara işaret edince okunur [S1][S3][S6]. Anthropic'in
mühendislik yazısı tasarımı "progressive disclosure" diye adlandırıyor ve
tetiklemeyi ad ile açıklamanın belirlediğini söylüyor [S8].

Zaman çizgisi: duyuru 2025-10-16 (claude.ai, Claude Code, API, SDK) [S7];
açık standart 2025-12-18, agentskills.io ve Apache-2.0 lisanslı spec
deposu [S9][S4]. Benimseme: OpenAI Codex standarttan önce, Aralık 2025'te
deneysel destek ekledi [S11][S10]; VS Code 1.108 (2026-01-08) [S17];
Cursor [S12]; Gemini CLI v0.23.0 (2026-01-07) [S13][S14]; GitHub CLI
`gh skill install` ile Copilot, Claude Code, Cursor, Codex ve Gemini'ye
tek komutla kurulum (2026-04-16) [S18]. agentskills.io'nun kendi listesi
kırk beş civarı ürün sayıyor; liste üreticinin kendi beyanı [S2].

Dizin konumu: spec konum tanımlamaz. Araçlar arası uzlaşma `.agents/skills/`
oldu; çoğu araç uyumluluk için `.claude/skills/`'i de tarıyor [S3][S10][S12].
Claude Code'un belgesi `.agents/skills/`'i listelemiyor [S5].

**Anlaşmazlık.** Alan katılığı yüzeye göre değişiyor: spec `name`'i zorunlu
ve klasör adıyla eş tutuyor; Claude Code her alanı isteğe bağlı sayıyor,
tanımadığı anahtarı sessizce yok sayıyor; claude.ai ve API yüklemesi ise
spec dışı her anahtarda hata veriyor [S5][S6]. Claude Code spec'te olmayan
bir düzine alan ekliyor (`when_to_use`, `disable-model-invocation`,
`context: fork`, `hooks`, `paths` …) [S5]. Sonuç: her yerde çalışacak bir
skill yalnızca altı spec alanını kullanmalı. Standardın yönetişimi
(Linux Foundation altında olduğu iddiası) yalnızca dördüncü basamak
kaynaklarda geçiyor, resmî sayfalarda yok; doğrulanmamış sayılır.

**Açık.** Bağımsız bir token tasarrufu ölçümü yok; rakamlar üreticinin.
Bir atölye makalesi topluluk skill'lerinin %26,1'inde güvenlik açığı
bulduğunu söylüyor [S19]; yalnızca özet okundu, örneklem boyutu
görülmedi.

### 2 · Skill yazmanın en iyi pratikleri: kim söylüyor, hangisi ölçülü?

**Uzlaşma.** Açıklama tek tetikleyicidir; "ne zaman kullanılır" bilgisi
gövdede değil açıklamada durur. Spec, Anthropic'in iki belgesi ve bir
tersine mühendislik yazısı aynı şeyi söylüyor; seçim istemci tarafında
anahtar kelime eşleşmesi değil, modelin açıklamalar üzerinde akıl
yürütmesi [S1][S30][S5][S38]. Gövde kısa tutulur (Anthropic: 500 satır
altı; uygulayıcılar: 200–500 kelime), yan dosyalar tek seviye derinlikte
[S30][S1][S36]. Deterministik iş betiğe alınır [S30][S8]. Skill yazmadan
önce skill'siz koşu yapılıp başarısızlıklar kaydedilir [S30][S8][S36].

Ölçümler 2026'da geldi ve hepsi hakem öncesi (preprint):

- **Progressive disclosure işe yarıyor, sınırlıyla.** Kontrollü deney:
  tek seviye açığa çıkarma derlem bağlama sığmayınca yardım ediyor
  (Haiku 4.5 tek kitap: ham 0,745 → düz 0,867; 20 kitap Codex: 0,257 →
  0,462, token 68,3M → 32,5M), ikinci bir yönlendirme seviyesi "hiç
  yardım etmiyor, bazen bozuyor" (0,885 → 0,640). Yazarların özeti:
  "bağlam satın alır, zekâ değil" [S34]. Bir şeyi kendi açıklamalı çok
  skill'e bölmemenin dolaylı kanıtı.
- **Skill'ler ortalamada az şey değiştiriyor.** 49 kamusal skill, 565
  görev, Claude Code + Haiku 4.5: 39 skill sıfır fark; ortalama +%1,2
  (89,8 → 91,0); token +%10,5; yedi skill +%30'a kadar kazanç, üçü −%10'a
  kadar zarar. Başarısızlık nedenleri: bilgi değil yetenek açığı, kapsam
  uyumsuzluğu ("kapsamlı referans" karar uzayını genişletiyor), sabit
  değerli şablonların yanlış kopyalanması, sürüm uyumsuzluğu [S35].
  Çalışma skill'in kaç kez yüklendiğini ölçmemiş; sıfır farkın bir
  kısmı tetiklenmeme olabilir.
- **Her zaman yüklü dosyalar pahalı, kazancı yok.** AGENTS.md/CLAUDE.md
  üzerine 300+138 görevlik çalışma: çözüm oranı anlamlı değişmiyor,
  maliyet %20'den fazla artıyor; geliştirici yazdığı dosya LLM'in
  yazdığından ~%7 iyi (p=0,038); dosyada adı geçen araç 1,6 kat
  kullanılıyor [S37]. "Olguları CLAUDE.md'ye, prosedürleri skill'e"
  tavsiyesinin arkasındaki en güçlü kanıt bu.
- **Tetiklenme darboğaz.** Akıllı sözleşme denetimi alanında 83 skill,
  7 yapılandırma: etkiyi model belirliyor, en iyi yapılandırmada +%22,8
  [S39]. Yalnızca özet okundu.

**Anlaşmazlık.**

- *İddialı açıklama mı, ölçülü mü?* skill-creator ve agentskills.io
  "Claude az tetikler, açıklama iddialı olsun" diyor [S31][S30].
  Anthropic'in istem rehberi ise Opus 4.5 ve sonrası için "fazla
  tetikleyebilir, agresif dili geri çekin; 'CRITICAL: You MUST' yerine
  'Use this tool when…'" diyor [S33]. Aynı üretici, iki belge,
  uzlaştırılmamış; cevap model nesline bağlı.
- *Yasak mı, olumlu tarif mi?* Anthropic'in skill belgesi kural
  uyulmayınca "MUST" ile sertleştirmeyi öneriyor [S30]; obra/superpowers
  gayriresmî karşılaştırmada yasak ifadenin istenmeyen çıktıyı
  artırdığını, olumlu tarifin daha iyi olduğunu bildiriyor [S36];
  Pocock aynı görüşte, kanıtsız [S32]. Üçüncü basamağın üstünde ölçüm yok.
- *Tetikleme ölçümü güvenilir mi?* Anthropic'in yöntemi (20 sorgu, 3 koşu,
  60/40 bölme) tek bir sonuç yayımlamış: altı skill'in beşinde iyileşme,
  rakam yok [S30][S29]. Açık bir hata kaydı aracın skill yönlendirmesini
  değil slash-komut çağrısını ölçtüğünü, aynı 22 sorguda dört
  açıklamanın da 10'da 1–2 pozitif, 12'de 12 negatif verdiğini gösteriyor;
  üründe doğrudan koşunca doğru yönlendirmiş [S40]. Tek kullanıcı, tek
  skill; Anthropic yanıtlamamış.

**Açık.** Üçüncü şahıs anlatım, ad biçimi, "emir mi gerekçe mi" ve
açıklama uzunluğu için hiçbir ölçüm yok; 500 satır sınırı hiçbir yerde
türetilmiyor. "Kısa açıklama daha iyi tetikler" folklor sayılır: herkes
söylüyor, kimse ölçmemiş.

### 3 · Skill'ler nasıl dağıtılıyor, popüler depoların ortak yanı ne?

**Uzlaşma.** Claude Code'da üç yol var: `.claude/skills/`'i depoya
commit etmek, bir eklenti (`plugin`) içine koymak, yönetilen ayarlarla
kuruma dağıtmak [S5]. Eklenti pazarı yalnızca içinde
`.claude-plugin/marketplace.json` olan bir git deposudur ("katalog,
barındırılan mağaza değil"); tek skill'li depoya bu dosya eklenince
`claude plugin install <ad> --marketplace owner/repo` çalışır [S20][S21].
Yayın öncesi liste: kalıcı kebab-case ad, sürüm numarasını her yayında
artır ya da hiç verme, `claude plugin validate --strict`, kök dizinde
README [S21]. claude.ai tarafında skill ZIP olarak yüklenir, varsayılan
olarak kişiseldir [S24]; üç yüzey (claude.ai, API, Claude Code) ayrı
depolardır, aralarında eşitleme yok [S6].

Araçlar arası dağıtımda fiilî standart Vercel'in `npx skills add
owner/repo` komutu: 79 ajan, sembolik bağla tek kopya, yalnızca ad ve
açıklama ister; skills.sh dizini (2026-01-20) yayın komutu olmadan,
kurulum telemetrisiyle dolar [S27][S28]. GitHub'ın `gh skill` komutu
aynı işi sağlayıcıdan yapıyor ve kaynak deposunu ön bölüme yazıyor [S18].

En çok yıldızlı iki topluluk deposu (obra/superpowers ~300k,
mattpocock/skills ~294k) aynı düzeni paylaşıyor: `skills/<ad>/SKILL.md`
monorepo, MIT, README'nin ilk ekranı ajan başına kurulum tablosu,
`.claude-plugin/` manifesti (depo aynı zamanda pazar), değişiklik günlüğü
[S25][S26]. Anthropic'in kendi deposu da aynı: yüzey başına bir kurulum
bloğu, `template/` başlangıç iskeleti, klasör başına lisans [S22].
Pocock'un README'si skill'leri "kim çağırır" (kullanıcı / model) diye
ikiye ayırıyor ve "eklenti ile skills.sh'ten ikisini kurma, ikisini de
kurarsan her skill iki kez gelir" uyarısı taşıyor [S26].

Güvenlik yönergesi her Anthropic yüzeyinde aynı: eklenti makinede rastgele
kod çalıştırabilir, `allowed-tools`'u inceleyin, `!` ile gömülen kabuk
komutu izin sormaz, "harici adresten veri çeken skill'ler özellikle
risklidir" [S23][S5][S6]. Risk ölçülmüş: Snyk'in 3.984 skill taraması
(OpenClaw ekosistemi) %36,8'inde en az bir sorun, %13,4'ünde kritik, 76
doğrulanmış zararlı [S42]; bir deney gizli talimatın dosya sızdırdığını
gösteriyor [S41b]; resmî pazardaki bir eklentide beş yükten beşi sır
sızdırdı, Anthropic "tasarlandığı gibi" diye kapattı [S43]. Yayımcı için
sonuç: betiksiz, hook'suz, harici çağrısız bir skill en küçük güven
yarıçapına sahip ve en kolay benimsenen [S23][S44b].

Adoption sinyali olarak yalnızca skills.sh telemetrisi ve GitHub yıldızı
var; telemetri kurulum olayı sayar, kullanıcı değil, ve "şunu da kur"
diyen skill'ler sayıyı şişirir [S28].

**Anlaşmazlık.** `.skill` dosyasının iç biçimi hiçbir resmî sayfada
yazmıyor; yardım merkezi yalnızca ZIP'ten söz ediyor [S24][S31].
Açıklama sınırı yüzeye göre 1.024 / 200 / 1.536 karakter [S1][S24][S5].
Üçüncü taraf bloglardaki yıldız sayıları GitHub'dakinden iki kata kadar
sapıyor; yalnızca GitHub sayfaları kullanıldı.

**Açık.** Hangi README ve düzen alışkanlığının benimsemeyi gerçekten
artırdığına dair kontrollü çalışma yok. Yukarıdaki "ortak düzen" bir
gözlem, bir neden-sonuç bulgusu değil.

### 4 · LLM'ler literatür tararken nerede yanılıyor, ne azaltıyor?

**Uzlaşma.**

- **Bellekten atıf uydurulur, kaynağa bağlanınca azalır, bitmez.**
  636 atıflık ölçüm: GPT-3.5'te %55, GPT-4'te %18 uydurma; gerçek
  olanların da %43 / %24'ü hatalı [S41]. Dar ve az çalışılmış konularda
  oran artıyor: genel derlemede %17, uzmanlaşmış derlemede %46 [S46]
  (yalnızca özet okundu, doğrulanmadı).
  Sistematik derleme aracı olarak parametrik LLM'in kesinliği ve
  duyarlılığı %9–14 [S47b]. Web'e bağlı sistemlerde uydurma URL %3–13;
  deep-research ajanları düz aramalı modellerden iki kat fazla uyduruyor
  (%10,7 / %4,8) [S44].
- **Doğrulama mekanizma olunca çalışıyor.** Aynı çalışmada bağlantı
  doğrulama aracı verilip düzeltme istendiğinde ölü veya uydurma bağlantı
  GPT-5.1'de %16,0'dan %0,6'ya, Claude Sonnet 4.5'te %4,9'dan %0,8'e
  indi [S44]. Skill'deki "sayfayı getir, snippet'e güvenme" cümlesinin
  talimattan mekanizmaya çevrilmesi gerektiğinin kanıtı.
- **Çalışan bağlantı ≠ desteklenen iddia.** Üretken arama motorlarında
  cümlelerin yarısı tam destekli, atıfların dörtte biri cümleyi
  desteklemiyor; atıf kesinliği algılanan faydayla ters orantılı
  (r = −0,96) [S48b]. 14 modelde: bağlantı %94–100 çalışıyor, konuyla
  ilgili %81–96, iddiayı destekleyen yalnızca %39–77 (en iyi Opus 4.5,
  %76,8) [S47]. Uzman görevlerinde atıf doğruluğu %78–94 [S49].
- **Daha çok arama daha az doğruluk.** Araç çağrısı 2'den 150'ye
  çıkınca iddia desteği ortalama 42 puan düşüyor (GPT-5.4: %78,6 → %16,7;
  Opus 4.6: %80,0 → %57,9); GPT-5.4 daha 10 çağrıda %45,9 [S47].
  Skill için sonuç: tur başına genişliğe tavan koy, sonda doğrula,
  "daha çok ara" deme.
- **Varsayılan çıktı tek taraflı ve kendinden emin.** Tartışmalı
  sorularda tek taraflı cevap %52–95, desteklenmeyen ifade %12–98, atıf
  doğruluğu %31–79; deep-research modu aşırı güveni düşürüyor ama tek
  taraflılığı değil [S48]. Kaynak tespit görevinde 1.600 sorgunun
  %60'ından fazlası yanlış, neredeyse hiç "bilmiyorum" yok, ücretli
  katmanlar daha emin biçimde yanlış [S50]. Skill'in "uzlaşma /
  anlaşmazlık / açık" üçlüsü bu bulguya karşılık geliyor.
- **Sözel güven kalibre değil.** Modeller görev zorluğuna insanlardan
  daha az duyarlı, aşırı güvenli; güveni cevaptan önce sormak aşırı
  güveni azaltıyor [S51] (yalnızca özet okundu, doğrulanmadı). Skill'in "güven: yüksek/orta/düşük" satırı
  ancak kart sayısından ve basamaktan türetilirse anlamlı, modelin
  kendi notuyla değil.
- **Kaynak kalitesi kuralsız kalınca SEO çöplüğüne kayıyor.** Anthropic'in
  üretim notu: ilk ajanlar akademik PDF yerine içerik çiftliklerini
  seçti, kaynak kalitesi sezgisi eklenince düzeldi; "birincil kaynak
  tercihi" puanlama rubriklerinde ayrı madde [S52]. Önce/sonra rakamı yok.
- **Kanıt hiyerarşisi literatürü merdiveni başlangıç sayar.** GRADE,
  çalışma türünü yalnızca başlangıç seviyesi yapar, sonra beş düşürme
  (yanlılık, tutarsızlık, dolaylılık, kesinsizlik, yayın yanlılığı) ve
  üç yükseltme alanıyla oynar; tutarsızlık açıkça raporlanır; PRISMA 2020
  kesinlik değerlendirmesini ve heterojenlik incelemesini zorunlu kılar
  [S53][S54][S55]. Eşleme: skill'in basamağı = GRADE başlangıç seviyesi;
  kanıt türü etiketi = kaba yanlılık vekili; uzlaşma/anlaşmazlık ayrımı =
  tutarsızlık; "güven" = GRADE kesinliği, ki *dolaylılık* (kaynak başka
  bir ortamı incelemiş) ve *kesinsizlik* (tek veri noktası) için
  düşürülmeli. Skill'de bu iki düşürme yok.

**Anlaşmazlık.** Aynı ürünün "atıf doğruluğu" değerlendirmeden
değerlendirmeye uçuyor: Perplexity DeepResearch Bench'te %90 [S49],
DeepTRACE'te %49–58 ve deep-research modunda %97,5 desteksiz ifade
[S48], Tow'da %37 yanlış [S50]. Ölçü farklı: URL çalışıyor mu, konuyla
ilgili mi, iddiayı destekliyor mu. Tek bir "doğruluk" rakamı vermek
yanıltıcı; üçü ayrı söylenmeli.

**Açık.** "Birincil kaynağı tercih etmek çıktıyı iyileştirir" tezini
doğrudan sınayan kontrollü çalışma yok; kanıt Anthropic'in üretim notu
ve canlı trafikte düşük güvenilirlikli alanların zaten az alıntılandığı
gözlemi [S52][S56]. Aynı modelde bağlanmalı/bağlanmasız karşılaştırma
yok; fayda çalışmalar arası çıkarım. Zorunlu bir "anlaşmazlık" bölümünün
sonucu iyileştirdiği ölçülmemiş; yalnızca varsayılanın tek taraflı olduğu
biliniyor. Uydurma atıflar yayımlanmış literatüre de sızıyor (2023 → 2025
arasında 12 kat artış, 10.000 makalede 4'ten 51'e) [S57]; ikincil
haberden okundu, Lancet aslı okunmadı; "bir makalede atıflanmış" artık
varlık kanıtı değil.

## Öneri

Depo ve tanıtım için: skill'i tek klasör, betiksiz, hook'suz ve harici
çağrısız tut; ön bölümde yalnızca altı spec alanını kullan (`metadata`
ile yazar ve sürüm ekle, `license` ekle) ki aynı klasör claude.ai'ye,
API'ye, Codex ve Cursor'a değişmeden gitsin [S1][S5][S6]. Depoya
`.claude-plugin/plugin.json` ve tek girdili `marketplace.json` ekle;
README'nin ilk ekranı ajan başına kurulum tablosu olsun (Claude Code
eklenti komutu, `npx skills add`, claude.ai ZIP), tek bir örnek rapor ve
MIT lisansı [S21][S22][S25][S26][S27]. Sürüm etiketi at; kuran kişi
etikete sabitleyebilsin [S44b].

Skill'in kendisi için, bu derlemenin doğrudan gerektirdiği dört değişiklik:

1. **Bağlantı doğrulama mekanizma olsun.** Kaynak tablosuna girmeden önce
   her URL gerçekten getirilsin ve "okundu / yalnızca snippet" ayrımı
   zorunlu kalsın; getirilemeyen kaynak alıntı değil ipucu sayılsın
   [S44].
2. **Tur başına genişlik tavanı.** Alt soru başına arama sayısına sınır,
   doymaya ulaşınca durma; "daha çok ara" yerine "sonda doğrula" [S47].
3. **Güven, modelin notu değil kart sayımı olsun.** Yüksek = en az iki
   bağımsız 1–2. basamak kaynak, yakın bağlam, son üç yıl; dolaylılık ve
   tek-kaynak durumunda bir seviye düşür (GRADE) [S53][S54]; S51
   yalnızca özetten, doğrulanmadı.
4. **Üç ayrı ölçü.** Rapor ve tanıtım "kaynaklı" demek yerine bağlantı
   çalışıyor mu, ilgili mi, iddiayı destekliyor mu diye üç ayrı şey
   söylesin [S47][S48b].

Tanıtımda dürüstçe söylenebilecekler: biçim açık standart ve kırka yakın
araç okuyor; bellekten atıf uydurma ölçülmüş bir sorun; skill'in tasarımı
literatürdeki üç başarısızlık biçimine (uydurma, desteksiz iddia, tek
taraflılık) birer karşılık koyuyor. Söylenemeyecek: skill'in sonucu
iyileştirdiği. Ölçmedik; literatür de skill'lerin ortalamada az şey
değiştirdiğini söylüyor [S35].

- **Güven:** orta. Dördüncü alt soruda sekiz 1. basamak ölçüm var ama
  hepsi genel deep-research ürünleri üzerine, bizim skill'imiz üzerine
  değil (dolaylılık). İkinci alt sorudaki üç ölçüm hakem öncesi ve tek
  model üzerinde. Dağıtım bulguları spec ve resmî belge, yüksek güven.
- **Öneriyi ne değiştirir:** skill'in kendi deneme setinde skill'li ve
  skill'siz koşuların iddia desteği oranı. Fark çıkmazsa (literatürün
  ortalaması bu) skill'i kısaltmak gerekir, uzatmak değil. Tetikleme
  aracındaki hata kaydı [S40] doğrulanırsa Anthropic'in tetikleme
  rakamları da yeniden ölçülmeli.
- **Gerilimler:** skill'in açıklaması skill-creator'ın "iddialı ol"
  tavsiyesiyle yazıldı; Anthropic'in istem rehberi yeni modellerde bunun
  fazla tetiklemeye yol açtığını söylüyor [S31][S33]. Hangi model
  nesliyle kullanılacağı belli değilse ölçülü dil daha güvenli. Karar
  kullanıcının.

## Kaynaklar

| # | Başlık | Yazar / kurum | Tarih | Basamak | Kanıt türü | Not |
|---|---|---|---|---|---|---|
| S1 | [Agent Skills Specification](https://agentskills.io/specification) | agentskills.io | 2025-12 | 1 | spesifikasyon | okundu |
| S2 | [Agent Skills overview + client list](https://agentskills.io/) | agentskills.io | güncel | 1 | spesifikasyon | okundu; liste öz beyan |
| S3 | [How to add skills support to your agent](https://agentskills.io/client-implementation/adding-skills-support.md) | agentskills.io | güncel | 1 | spesifikasyon | okundu |
| S4 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | agentskills | güncel | 1 | kaynak kod | okundu |
| S5 | [Skills — Claude Code docs](https://code.claude.com/docs/en/skills) | Anthropic | güncel | 1 | spesifikasyon | okundu (109k'nın 100k'sı) |
| S6 | [Agent Skills overview — platform docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | Anthropic | güncel | 1 | spesifikasyon | okundu |
| S7 | [Introducing Agent Skills](https://claude.com/blog/skills) | Anthropic | 2025-10-16 | 1 | üretim deneyimi | okundu |
| S8 | [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Zhang, Lazuka, Murag / Anthropic | 2025-10-16, güncelleme 2025-12-18 | 2 | üretim deneyimi | okundu |
| S9 | [Skills for organizations, partners, the ecosystem](https://claude.com/blog/organization-skills-and-directory) | Anthropic | 2025-12-18 | 1 | duyuru | okundu |
| S10 | [Build skills — Codex/ChatGPT](https://learn.chatgpt.com/docs/build-skills) | OpenAI | güncel | 1 | spesifikasyon | okundu |
| S11 | [OpenAI are quietly adopting skills](https://simonwillison.net/2025/Dec/12/openai-skills/) | Simon Willison | 2025-12-12 | 3 | üretim deneyimi | okundu |
| S12 | [Agent Skills — Cursor docs](https://cursor.com/docs/skills) | Cursor | tarihsiz | 1 | spesifikasyon | okundu |
| S13 | [Agent Skills — Gemini CLI docs](https://geminicli.com/docs/cli/skills/) | Google | 2026-04-30 | 1 | spesifikasyon | okundu |
| S14 | [Gemini CLI Weekly Update v0.23.0](https://github.com/google-gemini/gemini-cli/discussions/16084) | google-gemini | 2026-01-07 | 1 | duyuru | okundu |
| S15 | [About agent skills — GitHub Docs](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) | GitHub | tarihsiz | 1 | spesifikasyon | okundu |
| S16 | [Agent Skills — VS Code docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills) | Microsoft | tarihsiz | 1 | spesifikasyon | okundu |
| S17 | [VS Code v1.108 release notes](https://code.visualstudio.com/updates/v1_108) | Microsoft | 2026-01-08 | 1 | sürüm notu | okundu |
| S18 | [Manage agent skills with GitHub CLI](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/) | GitHub | 2026-04-16 | 1 | duyuru | okundu |
| S19 | [Agent Skills for LLMs: Architecture, Acquisition, Security…](https://arxiv.org/abs/2602.12430) | Xu & Yan | 2026-02-12 / v4 2026-06-02 | 1 (atölye) | ölçüm | yalnızca özet |
| S20 | [Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace) | Anthropic | güncel | 1 | spesifikasyon | okundu |
| S21 | [Publish and distribute a plugin](https://code.claude.com/docs/en/plugins/publish) | Anthropic | güncel | 1 | spesifikasyon | okundu |
| S22 | [anthropics/skills](https://github.com/anthropics/skills) | Anthropic | 2026-10-16 okuma | 1 | kaynak kod | okundu |
| S23 | [Plugin security and trust](https://code.claude.com/docs/en/plugins/security) | Anthropic | güncel | 1 | spesifikasyon | okundu |
| S24 | [Use skills in Claude — Help Center](https://support.claude.com/en/articles/12512180-use-skills-in-claude) | Anthropic | ~2026-09 | 1 | spesifikasyon | okundu |
| S25 | [obra/superpowers](https://github.com/obra/superpowers) | Jesse Vincent | 2026-10-16 okuma | 1 / 3 | kaynak kod | okundu |
| S26 | [mattpocock/skills](https://github.com/mattpocock/skills) | Matt Pocock | 2026-10-16 okuma | 1 / 3 | kaynak kod | okundu |
| S27 | [Introducing skills, the open agent skills ecosystem](https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem) · [vercel-labs/skills](https://github.com/vercel-labs/skills) | Vercel | 2026-01-20 | 1 | spesifikasyon | okundu |
| S28 | [skills.sh leaderboard](https://skills.sh/) · [docs](https://skills.sh/docs) | Vercel | 2026-10-16 okuma | 2 | telemetri | okundu; kurulum olayı, kullanıcı değil |
| S29 | [Improving skill-creator: test, measure, refine](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills) | Anthropic | 2026-03-03 | 2 | üretim (tek rakam) | okundu |
| S30 | [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) · [Optimizing skill descriptions](https://agentskills.io/skill-creation/optimizing-descriptions) | Anthropic / agentskills.io | güncel | 1 | görüş + yöntem | okundu |
| S31 | [skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | Anthropic | güncel | 1 | üretim deneyimi | okundu |
| S32 | [writing-for-agents SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md) | Matt Pocock | güncel | 3 | görüş | okundu |
| S33 | [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Anthropic | güncel | 1 | görüş / üretim | okundu |
| S34 | [Is Progressive Disclosure All You Need for Long-Context Agents?](https://arxiv.org/html/2607.17598v1) | He, Zhao, Wang, Chen | 2026-07-20 | 1 (preprint) | deney | okundu |
| S35 | [SWE-Skills-Bench](https://arxiv.org/html/2603.15401) | Han et al. | 2026-03-16 | 1 (preprint) | ölçüm | okundu |
| S36 | [writing-skills SKILL.md — obra/superpowers](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md) | Jesse Vincent | güncel | 3 | üretim + gayriresmî deney | okundu |
| S37 | [Evaluating AGENTS.md](https://arxiv.org/html/2602.11988) | Gloaguen et al. | 2026-02-12 / v3 2026-09-29 | 1 (preprint) | ölçüm | okundu |
| S38 | [Claude Agent Skills: A First Principles Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/) | Han Lee | 2025-10-26 | 3 | tersine mühendislik | okundu; URL bu oturumda doğrulandı |
| S39 | [Demystifying Agent Skills for Smart Contract Auditing](https://arxiv.org/abs/2609.29454) | Gao et al. | 2026-09-24 | 1 (preprint) | ölçüm | yalnızca özet |
| S40 | [Issue #6253: trigger eval measures slash-command invocation](https://github.com/anthropics/claude-plugins-official/issues/6253) | Kevin-Chen0 | 2026-09-18 | 4 (birincil veri) | ölçüm, n=1 | okundu; yanıtsız |
| S41 | [Fabrication and errors in the bibliographic citations generated by ChatGPT](https://www.nature.com/articles/s41598-023-41032-5) | Walters & Wilder, Sci Rep | 2023-09-07 | 1 | ölçüm | okundu |
| S41b | [Agent Skills Enable a New Class of … Prompt Injections](https://arxiv.org/abs/2510.26328) | Schmotz, Abdelnabi, Andriushchenko | 2025-10-30 | 1 (preprint) | deney | yalnızca özet |
| S42 | [ToxicSkills](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) | Snyk | 2026-02 | 2 | ölçüm (satıcı) | okundu; OpenClaw ekosistemi |
| S43 | [Skills, Connectors, Plugins, Oh My](https://pluto.security/blog/claude-extension-ecosystem-security-practitioner-guide/) | Perkal / Pluto Security | 2026-04-29 | 2 / 3 | deney | okundu |
| S44 | [Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents](https://arxiv.org/html/2604.03173) | Rao, Wong, Callison-Burch | 2026-04 | 1 (preprint) | ölçüm + deney | okundu |
| S44b | [Securing Claude Code plug-ins](https://developers.redhat.com/articles/2026/08/18/securing-claude-code-plug-ins-best-practices-repository-security) | Kapner / Red Hat | 2026-08-18 | 3 | uygulayıcı rehberi | okundu |
| S46 | [Influence of Topic Familiarity and Prompt Specificity on Citation Fabrication](https://mental.jmir.org/2025/1/e80371) | Linardon et al., JMIR Ment Health | 2025-11-12 | 1 | deney | yalnızca özet (Europe PMC) |
| S47 | [Cited but Not Verified](https://arxiv.org/html/2605.06635v1) | Onweller et al., PwC | 2026-05-07 | 1 (preprint) | deney | okundu |
| S47b | [Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews](https://www.jmir.org/2024/1/e53164) | Chelli et al., JMIR | 2024-05-22 | 1 | ölçüm | özet (Europe PMC) |
| S48 | [DeepTRACE](https://arxiv.org/html/2509.04499) | Venkit et al. | 2025-09-02 | 1 (preprint) | ölçüm | okundu |
| S48b | [Evaluating Verifiability in Generative Search Engines](https://arxiv.org/abs/2304.09848) | Liu, Zhang, Liang, EMNLP Findings | 2023 | 1 | ölçüm | okundu |
| S49 | [DeepResearch Bench](https://arxiv.org/html/2506.11763v1) | Du et al. | 2025-06-13 | 1 (preprint) | ölçüm | okundu |
| S50 | [AI Search Has a Citation Problem](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php) | Jaźwińska & Chandrasekar, Tow Center | 2025-03-06 | 2 | ölçüm | okundu |
| S51 | [Do Language Models Mirror Human Confidence?](https://arxiv.org/abs/2506.00582) | Xu et al., ACL 2025 Findings | 2025-07-28 | 1 | deney | yalnızca özet |
| S52 | [How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system) | Anthropic | 2025-06-13 | 2 | üretim deneyimi | okundu |
| S53 | [Cochrane Handbook ch. 14](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14) | Schünemann et al. | güncel | 1 | spesifikasyon | okundu |
| S54 | [GRADE Handbook](https://gdt.gradepro.org/app/handbook/handbook.html) | GRADE Working Group | güncel | 1 | spesifikasyon | okundu (ilk 100k) |
| S55 | [The PRISMA 2020 statement](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583) | Page et al., PLoS Med | 2021-03-29 | 1 | spesifikasyon | okundu; kontrol listesi görsel |
| S56 | [News Source Citing Patterns in AI Search Systems](https://arxiv.org/html/2507.05301) | Kai-Cheng Yang | 2025-07-07 | 1 (preprint) | ölçüm | okundu |
| S57 | [Review uncovers rising rate of fake references](https://www.cidrap.umn.edu/anti-science/review-uncovers-rising-rate-fake-references-published-biomedical-papers) | CIDRAP, Topaz et al. (Lancet) üzerine | 2026 | 2 | ölçüm (ikincil) | okundu; Lancet aslı okunmadı |

Okunamayan ve alıntılanmayan kaynaklar: OpenAI "Introducing deep research"
blog yazısı (403), OCEBM 2011 seviye sayfası (403), Anthropic'in "Complete
Guide to Building Skills" PDF'inin dağıtım bölümü (ikinci ajan okudu,
üçüncü okumadı), üçüncü taraf "en iyi skill depoları" yazıları (yıldız
sayıları GitHub'la uyuşmadı).
