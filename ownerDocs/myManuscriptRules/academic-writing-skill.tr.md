# Genel Akademik Makale Yazım, Düzenleme ve Tutarlılık Skill'i

> **SOURCE VERSION — NOT the operative one.** This Turkish file is the owner's authoring
> source, kept for reading and revision. The file that BINDS manuscript work is the English
> `academic-writing-skill.md` beside it; when the two disagree, the English file wins.
> An edit here does NOT propagate: re-running the audited translation pass is what makes it
> operative. Both are stack-managed — edit them in
> `claude-agent-stack/templates/ownerDocs/`, never in a repo copy.

Bu belge, farklı disiplinlerdeki ampirik, teorik, hesaplamalı ve metodolojik çalışmaların yazılması veya yeniden düzenlenmesi için kullanılabilecek genel bir kural setidir. Amaç yalnızca metni daha akademik göstermek değil; araştırma sorusu, yöntem, bulgu, yorum ve katkı arasında denetlenebilir bir bilimsel argüman kurmaktır.

Bu kurallar bir yazara, editöre veya LLM tabanlı yazım aracına doğrudan talimat olarak verilebilir.

---

## 0. Öncelik sırası ve bağlayıcı ilkeler

Bir makale düzenlenirken aşağıdaki öncelik sırası izlenmelidir:

1. **Hedef derginin güncel author guidelines'ı**
2. **Çalışma türüne özgü reporting guideline**
3. **Bilimsel ve sayısal doğruluk**
4. **İddia ile kanıt arasındaki uyum**
5. **Bölümler arası semantik ve sayısal tutarlılık**
6. **Yazarın bilinçli terminoloji ve biçim tercihleri**
7. **Akademik ton, akıcılık ve kısalık**

Hedef dergi bir kuralı açıkça farklı tanımlıyorsa bu genel belge değil, dergi kuralı uygulanmalıdır. Randomized trials, observational studies, systematic reviews, prediction models, qualitative studies, animal experiments ve benzeri tasarımlar için uygun reporting checklist ayrıca kullanılmalıdır.

### Mutlak olarak korunması gerekenler

- Veri, sayı, denklem, sonuç, citation, tablo ve figure bilgisi uydurulmamalıdır.
- Metni akıcı hale getirmek amacıyla bilimsel anlam değiştirilmemelidir.
- Yazarın bilerek İngilizce bıraktığı teknik terimler izinsiz çevrilmemelidir.
- LaTeX commands, labels, refs, citations, macros, equations, tables ve figures bozulmamalıdır.
- Bilimsel iddia, tasarımın ve verinin izin verdiğinden daha güçlü hale getirilmemelidir.
- Eksik veya çelişkili bilgi sessizce tamamlanmamalı; `[DOĞRULANMALI]` veya editoryal not ile işaretlenmelidir.

---

## 1. Uzlaştırılmış temel kararlar

Bu kural setinde bazı yaygın fakat aşırı katı yaklaşımlar aşağıdaki biçimde dengelenmiştir.

### 1.1 Pasif anlatım varsayılandır; fakat mekanik bir zorunluluk değildir

Akademik metin kişisiz, ölçülü ve nesne/işlem odaklı yazılmalıdır. Özellikle Methods bölümünde pasif yapı sıklıkla uygundur. Bununla birlikte, failin bilinmesi önemliyse veya pasif yapı cümleyi yapaylaştırıyorsa aktif cümle kullanılmalıdır.

**Uygun:**

> Veriler bootstrap procedure ile analiz edilmiştir.

**Uygun:**

> \citet{ornek2025}, aynı effect'in larger models üzerinde azaldığını bildirmiştir.

**Uygun olmayan mekanik pasiflik:**

> Tarafımızca literatürün gösterilmiş olduğu görülmektedir.

Akademik ton, faili gizlemek değil; iddiayı ölçülü ve denetlenebilir biçimde sunmak anlamına gelir.

### 1.2 Tense, bölüm adına değil retorik işleve göre seçilmelidir

Makalenin tamamı present simple ile yazılmamalıdır. Genel bilgi, önceki çalışma, yürütülen yöntem, gözlenen sonuç ve mevcut yorum farklı zaman kipleri gerektirir.

### 1.3 Çok sayıda alt başlık kullanılmamalıdır; ancak gerekli yapısal ayrım engellenmemelidir

Abstract, Introduction, Methods, Results, Discussion ve Conclusion temel omurgadır. Methods ve Results, çalışmanın yapısı gerektiriyorsa alt başlıklara ayrılabilir. Genel olarak üçten fazla heading level kullanılmamalıdır. Her iki veya üç paragraf için yeni bir alt başlık açılmamalıdır.

### 1.4 Her literatür çalışması tek tek anlatılmamalıdır

Amaç literatürde bulunan her makaleyi veya her yöntemi saymak değil, araştırma sorusunu kuran **materially relevant method families, findings ve limitations**'ı sentezlemektir. Kapsayıcılık, kataloglama ile karıştırılmamalıdır.

### 1.5 Her Discussion bölümünde karşılaştırma tablosu zorunlu değildir

Prior work ile karşılaştırma çok boyutluysa ve prose içinde takip edilmesi zorlaşıyorsa comparison table kullanılmalıdır. Tablo yalnızca dekoratif veya zorunluymuş gibi eklenmemelidir.

### 1.6 Her bölümde acronym yeniden tanımlama genel standart değildir

Minimum kural şudur: abbreviation abstract içinde ilk kullanımda, main text içinde ise yeniden ilk kullanımda tanımlanmalıdır. Uzun ve bağımsız okunabilen major sections, supplementary files, figures ve tables içinde gerekirse yeniden açılmalıdır. Yazarın daha katı house style'ı uygulanacaksa her **major section** içindeki ilk kullanımda yeniden tanımlama yapılabilir; her subsection'da mekanik tekrar yapılmamalıdır.

### 1.7 “Proposed method” yalnızca gerçekten yeni bir yöntem varsa kullanılmalıdır

Çalışma yeni bir algorithm önermiyor; bir evaluation, ablation, measurement instrument veya empirical analysis sunuyorsa bunlar doğru adlarıyla tanımlanmalıdır. Her araştırma artefaktına otomatik olarak “proposed framework” denmemelidir.

---

## 2. Makalenin bilimsel omurgası

Makale aşağıdaki zincir üzerinden kurulmalıdır:

> **Genel problem → mevcut bilgi → literatürdeki gerilim veya boşluk → araştırma sorusu → tasarım/yöntem → bulgu → yorum → katkı → sınır**

Her bölüm bu zincirin kendisine ait kısmını taşımalıdır.

### Yapılmalı

- Araştırma sorusu tek cümleyle ifade edilebilmelidir.
- Her headline claim doğrudan bir test, table, figure veya analysis ile eşlenmelidir.
- Çalışmanın özgünlüğü, hangi confound'u ayırdığı, hangi baseline'ı kurduğu veya hangi problemi çözdüğü üzerinden gösterilmelidir.
- Contribution, yalnızca “novel” sözcüğüyle değil, **kanıt zinciriyle** kurulmalıdır.
- Her major claim için population, setting, endpoint ve design boundary belirtilmelidir.

### Yapılmamalı

- Araştırma sorusu bölümden bölüme değiştirilmemelidir.
- Introduction'da vaat edilmeyen yeni bir ana katkı Conclusion'da eklenmemelidir.
- Results'ta bulunmayan bir bulgu Discussion'da ortaya çıkarılmamalıdır.
- Bir correlation, causal effect veya mechanism olarak sunulmamalıdır.
- Hikâyeyi güçlendirmek amacıyla result olduğundan daha uniform, robust veya general gösterilmemelidir.

---

## 3. Akademik dil, voice ve tense kuralları

### 3.1 Akademik ton

Metin:

- kişisiz,
- ölçülü,
- açık,
- kanıt-temelli,
- fail bakımından gerektiğinde belirgin,
- jargon bakımından disipline uygun,
- abartısız

olmalıdır.

#### Tercih edilen kalıplar

- “Bu çalışmada X problemi ele alınmaktadır.”
- “X etkisinin Y bileşeninden kaynaklanıp kaynaklanmadığı test edilmiştir.”
- “Veriler Z procedure kullanılarak analiz edilmiştir.”
- “Statistically detectable bir difference gözlenmiştir.”
- “Bu pattern, X explanation'ı ile uyumludur.”
- “Sonuç, Y population ve Z setting ile sınırlıdır.”

#### Kaçınılması gereken kalıplar

- “Biz kesin olarak kanıtladık ki…”
- “Çok çarpıcı ve şaşırtıcı bir sonuç elde ettik.”
- “Herkesin bildiği gibi…”
- “Kolayca görülebileceği üzere…”
- “Bu yöntem kuşkusuz en iyisidir.”
- “Sonuçlar devrim niteliğindedir.”

“Prove”, “demonstrate conclusively”, “always”, “never”, “safe”, “guaranteed” ve benzeri ifadeler yalnızca gerçekten gerekli evidential standard karşılandığında kullanılmalıdır.

### 3.2 Tense matrisi

| Retorik işlev | Tercih edilen tense | Örnek işlev |
|---|---|---|
| Genel kabul gören bilgi | Present simple | “LLMs generate code from natural-language prompts.” |
| Hâlen geçerli bir literature state | Present perfect veya present simple | “Several studies have examined…” |
| Belirli geçmiş çalışma | Past simple | “Smith et al. reported…” |
| Bu çalışmada yapılan işlem | Past simple; çoğunlukla passive | “The models were evaluated…” |
| Definition, equation veya figure'ın mevcut işlevi | Present simple | “Equation~(1) defines…”; “Figure~1 shows…” |
| Gözlenen result | Past simple | “The treatment produced…” |
| Result'ın mevcut anlamı | Present simple | “These findings indicate…” |
| Belirsiz interpretation | Modal + present | “This pattern may reflect…” |
| Future work | Future veya modal | “Future studies should examine…” |

#### Bölüm bazında varsayılan kullanım

- **Abstract:** background present; yöntem ve bulgular past; take-home implication present.
- **Introduction:** established knowledge present; belirli prior studies past; literature evolution present perfect; gap ve current objective present.
- **Methods:** yapılan işlemler past; definitions, equations ve general procedures present.
- **Results:** observed outcomes past; figures/tables present; çok sınırlı statistical interpretation present.
- **Discussion:** kendi bulgularına referans verirken past; anlam ve implication için present; mechanism belirsizliği için modal.
- **Conclusion:** çalışmada ne yapıldığı past; desteklenen nihai çıkarım present; future work future/modal.

#### Yapılmamalı

- Aynı paragrafta gerekçesiz tense drift yapılmamalıdır.
- Önceki bir çalışma sanki hâlen yürütülüyormuş gibi present tense ile anlatılmamalıdır.
- Kendi gözlenen sonuçları genel yasa gibi present simple ile sabitleştirilmemelidir.
- Tüm Methods bölümü present tense ile yazılmamalıdır.
- Tüm makale sırf “academic” görünsün diye passive voice'a zorlanmamalıdır.

### 3.3 Cümle ve paragraf yapısı

Her cümlede tercihen tek ana claim bulunmalıdır. Her paragraf tek bir argüman birimi olmalıdır.

İyi bir paragraf çoğunlukla şu sırayı izler:

1. Konu cümlesi
2. Evidence veya açıklama
3. Sınırlı interpretation
4. Sonraki paragrafa geçiş

#### Yapılmalı

- Ana fikir cümlenin erken kısmında verilmelidir.
- Uzun cümleler yöntem, sonuç, yorum ve limitation içeriyorsa bölünmelidir.
- Paragraflar genellikle 3--6 cümlelik anlam birimleri olmalıdır.
- “Bu”, “bunlar”, “söz konusu durum” gibi göndergeler açık olmalıdır.

#### Yapılmamalı

- Bir cümlede dört farklı claim birleştirilmemelidir.
- Aynı paragrafta literature review, method detail, result ve recommendation karıştırılmamalıdır.
- Metadiscourse, asıl argümanın önüne geçmemelidir.
- Aynı sonuç farklı kelimelerle tekrar tekrar anlatılmamalıdır.

---

## 4. Bölüm yapısı ve heading kullanımı

Genel araştırma makalesi omurgası şöyledir:

1. Title
2. Abstract
3. Keywords
4. Introduction
5. Methods / Materials and Methods
6. Results
7. Discussion
8. Conclusion veya Discussion içine entegre conclusion
9. Acknowledgements
10. Funding
11. Author Contributions
12. Competing Interests / Conflict of Interest
13. Ethics / Consent statements, gerekiyorsa
14. Data Availability
15. Code Availability, gerekiyorsa
16. References
17. Supplementary Information veya Appendix

Bu sıralama venue'ye göre değişebilir.

### Heading kuralları

- Core story gereksiz alt başlıklara bölünmemelidir.
- Introduction çoğu durumda tek başlık altında kalmalıdır.
- “Related Work” ve “Present Work” yalnızca disiplin veya venue bunu gerektiriyorsa ayrı başlık yapılmalıdır.
- Methods alt başlıkları gerçek workflow'dan türetilmelidir.
- Results alt başlıkları preregistered analysis hierarchy veya research questions ile hizalanmalıdır.
- Discussion alt başlıkları çok uzun metinlerde kullanılabilir; kısa tartışmalarda her paragraf için başlık açılmamalıdır.
- En fazla üç heading level kullanılmalıdır, venue aksini istemedikçe.

### Yapılmamalı

- İki cümlelik alt bölümler oluşturulmamalıdır.
- Başlıklar sonuç cümlesi veya pazarlama sloganı gibi yazılmamalıdır.
- Aynı içerik hem main text hem appendix içinde tekrar edilmemelidir.
- Hedef derginin article type yapısı görmezden gelinmemelidir.

---

## 5. Terminoloji, abbreviations ve notation

### 5.1 Terminoloji

Her temel kavram için tek bir canonical terim seçilmelidir.

#### Yapılmalı

- `task`, `unit`, `item`, `sample`, `case`, `arm`, `condition`, `endpoint`, `metric` ve `baseline` birbirinden ayrılmalıdır.
- Aynı concept bütün bölümlerde aynı adla kullanılmalıdır.
- Benzer görünen fakat farklı metrics açıkça tanımlanmalıdır.
- Teknik terimlerin Türkçe mi İngilizce mi bırakılacağı baştan belirlenmelidir.
- Yazarın bilerek İngilizce bıraktığı kelimeler korunmalıdır.

#### Yapılmamalı

- Aynı şey için sürekli farklı eşanlamlılar kullanılmamalıdır.
- “Validation”, “verification”, “confirmation”, “certification” ve “replication” rastgele karıştırılmamalıdır.
- Bir control, daha sonra baseline veya treatment olarak yeniden adlandırılmamalıdır.

### 5.2 Abbreviations

- Abstract, bağımsız bir metin gibi ele alınmalı ve abbreviation ilk kullanımda burada tanımlanmalıdır.
- Main text içinde abbreviation yeniden ilk kullanımda açılmalıdır.
- Uzun veya bağımsız okunabilen major sections içinde first use yeniden açılabilir.
- Tables, figures ve supplementary files mümkün olduğunca kendi içinde anlaşılabilir olmalıdır.
- Non-standard abbreviations minimumda tutulmalı ve yalnızca tekrar kullanım anlamlıysa oluşturulmalıdır.
- Title içinde yalnızca alan genelinde yerleşik abbreviations kullanılmalıdır.

#### House-style strict mode

Yazar her major section'ın bağımsız okunmasını istiyorsa abbreviation, Abstract, Introduction, Methods, Results, Discussion ve Conclusion içindeki ilk kullanımda yeniden tanımlanabilir. Aynı abbreviation her subsection'da yeniden tanımlanmamalıdır.

### 5.3 Symbols ve units

- Her symbol ilk kullanımda tanımlanmalıdır.
- Birim varsa belirtilmelidir.
- SI units tercih edilmelidir, alan standardı farklı değilse.
- Aynı symbol farklı anlamlarda kullanılmamalıdır.
- Scalar, vector, matrix ve set notation tutarlı olmalıdır.

---

## 6. Title ve Keywords

### 6.1 Title

Title, çalışmanın temel objesini, intervention veya method'unu ve gerekli ise study design'ı açıkça belirtmelidir.

#### Yapılmalı

- Spesifik ve bilgilendirici olmalıdır.
- Ana endpoint veya phenomenon gerektiğinde görünür olmalıdır.
- Study type, yanlış anlaşılmayı önlüyorsa title'a eklenmelidir.
- Claim strength, ana bulgudan daha güçlü olmamalıdır.

#### Yapılmamalı

- “Novel”, “revolutionary”, “unprecedented” gibi promotional sıfatlar kullanılmamalıdır.
- Sonuç causality göstermiyorsa causal title yazılmamalıdır.
- Aşırı uzun, iki noktalı ve üç iddialı title oluşturulmamalıdır.
- Non-standard abbreviations kullanılmamalıdır.

### 6.2 Keywords

- Genellikle 4--8 keyword seçilmelidir, venue'ye göre.
- Title'daki kelimelerin tamamı tekrar edilmemelidir.
- Method, domain, task ve ana phenomenon dengeli biçimde temsil edilmelidir.
- Alanın indexing terminology'si kullanılmalıdır.

---

## 7. Abstract kuralları

Abstract, venue aksini istemedikçe tek paragraf ve kendi başına anlaşılabilir olmalıdır. Genel hareket genelden özele doğru ilerlemelidir.

### Önerilen semantik sıra

1. **Genel problem:** Alan veya deployment context içinde hangi problem bulunmaktadır?
2. **Literature gap:** Önceki çalışmalar neyi birlikte ele almakta veya hangi comparison'ı eksik bırakmaktadır?
3. **Bu çalışmanın cevabı:** Hangi method, design, framework veya analysis sunulmaktadır?
4. **Deney ortamı:** Nerede, hangi sample/population ve hangi temel protocol ile test edilmiştir?
5. **Ana results:** Contribution'ı kanıtlayan iki veya üç headline result nedir?
6. **Take-home conclusion:** Sonuç ne anlama gelmektedir ve hangi scope ile sınırlıdır?

### Yapılmalı

- İlk 1--2 cümlede problem ve gap verilmelidir.
- “To address this problem, … is proposed/presented/evaluated” türü kalıplar yalnızca gerçekten uygun olduğunda kullanılmalıdır.
- Methods ayrıntıya boğulmadan sample, dataset, model/population, design ve endpoint belirtilmelidir.
- En önemli quantitative results verilmelidir.
- Effect size, uncertainty veya exact comparison, katkının anlaşılması için gerekliyse kullanılmalıdır.
- Son cümle contribution ile boundary'yi birlikte taşımalıdır.
- Background present, procedures/results past, implications present tense ile yazılmalıdır.

### Yapılmamalı

- Uzun literature review yapılmamalıdır.
- Hardware brand, file count, minor hyperparameters veya secondary tests ile abstract doldurulmamalıdır.
- Abstract'ta bütün p-values ve bütün subgroup results verilmemelidir.
- Citation kullanılmamalıdır, venue açıkça izin vermedikçe.
- Abstract, Introduction'ın ilk paragrafının kopyası olmamalıdır.
- Limitations tamamen gizlenmemelidir.
- Sonuçtan daha güçlü deployment veya generalization claim'i kurulmamaldır.

### Abstract için kısa kontrol

- Problem açık mı?
- Gap test edilebilir mi?
- Çözüm tek cümlede anlaşılır mı?
- Nerede ve nasıl test edildiği belli mi?
- Ana sonuçlar rakamla destekleniyor mu?
- Son cümle katkı ve scope'u içeriyor mu?

---

## 8. Introduction kuralları

Introduction, bütün makalenin koni biçimindeki hikâyesini kurmalıdır. Amaç yalnızca background vermek değil, okuyucuyu araştırma sorusuna zorunlu biçimde ulaştırmaktır.

### 8.1 Önerilen paragraf işlevleri

#### Paragraf 1 — En genel problem ve pratik bağlam

- Alanın geniş problemi tanımlanmalıdır.
- Problemin neden önemli olduğu gösterilmelidir.
- Factual claims güncel ve uygun references ile desteklenmelidir.
- Paragraf sonunda bir sonraki problem alanına geçiş hazırlanmalıdır.

#### Paragraf 2 — Yerleşik yaklaşım ve olumlu evidence

- Problemi çözmek için geliştirilen principal method families sentezlenmelidir.
- Hangi koşullarda başarılı oldukları belirtilmelidir.
- Çalışmalar tek tek kataloglanmamalıdır.

#### Paragraf 3 — Çelişkili veya negatif evidence

- Yerleşik yaklaşımın hangi regimes'de çalışmadığı gösterilmelidir.
- Model scale, dataset, training condition, budget veya evaluation weakness gibi moderating factors açıklanmalıdır.
- Paragraf, çözülmemiş problemle bitmelidir.

#### Paragraf 4 — Doğru baseline ve identification gap

- Gerçek practitioner veya scientific decision problem tanımlanmalıdır.
- Önceki çalışmaların hangi ingredients, controls veya explanations'ı ayıramadığı açıkça belirtilmelidir.
- Gap, “az çalışma vardır” gibi belirsiz değil, test edilebilir olmalıdır.

#### Paragraf 5 — Bu çalışmada sunulan yaklaşım

- “Bu nedenlerle…” geçişiyle current study tanıtılmalıdır.
- Ne test edildiği, hangi comparison'ın kurulduğu ve hangi gap'in hedeflendiği verilmelidir.
- Burada metodun ana fikri anlatılmalı; operation-level ayrıntıya girilmemelidir.
- Cümleler çoğunlukla kişisiz ve pasif olabilir.

#### Paragraf 6 — Contributions ve headline findings

- Empirical, methodological, theoretical ve practical contributions birbirinden ayrılmalıdır.
- Contributions tercihen 3--5 maddeyi geçmemelidir.
- Her madde bir **problem → çözüm/test → evidence → boundary** mini-zinciri içermelidir.
- Contribution listesi venue'nin stiline uygunsa kullanılmalıdır; aksi halde prose içinde verilmelidir.

#### Son paragraf — Scope ve roadmap

- Claim'in sınırı açıkça belirtilmelidir.
- Paper organization yalnızca okuyucuya gerçek navigasyon sağlıyorsa kısa biçimde verilmelidir.

### 8.2 Introduction içinde yapılmalı

- Her paragraf bir sonrakinin mantıksal ihtiyacını hazırlamalıdır.
- Literature chronological list yerine problem-solving narrative olarak kullanılmalıdır.
- Relevant method families ve unresolved problems dengeli sunulmalıdır.
- Positive ve negative literature birlikte değerlendirilmelidir.
- Study aim, research questions veya hypotheses açıkça belirtilmelidir.
- Novelty, hangi control veya design ile sağlandığı üzerinden gösterilmelidir.

### 8.3 Introduction içinde yapılmamalı

- Bütün Methods details verilmemelidir.
- Results bölümü baştan yeniden yazılmamalıdır.
- Contribution'ı büyütmek için prior work karikatürize edilmemelidir.
- “Yazarın bilgisine göre ilk” ifadesi güncel ve sistematik search olmadan kullanılmamalıdır.
- Aynı gap farklı paragraflarda tekrar tekrar söylenmemelidir.
- “Related Work” ve “Present Work” başlıkları disiplin gerektirmedikçe eklenmemelidir.
- Her citation ayrı cümleyle özetlenmemelidir.
- “Tüm yöntemler” sunulmaya çalışılırken ana hikâye kaybedilmemelidir.

---

## 9. Methods kuralları

Methods bölümünün temel görevi, okuyucunun çalışmayı anlayabilmesi, değerlendirebilmesi ve mümkün olduğunca yeniden üretebilmesidir.

### 9.1 Açılış paragrafı

İlk paragrafta:

- genel study design,
- ana method/framework/instrument,
- input-output flow,
- primary endpoint,
- ana subsections

kısaca verilmelidir.

Çalışma karmaşık bir pipeline içeriyorsa, overall framework figure ilk bölümde sunulmalıdır. Figure, parçaların sırasını ve bağlantılarını göstermeli; metin, figure'ı yalnızca tekrar etmemeli, mantığını açıklamalıdır.

### 9.2 Subsection yapısı

Subsections çalışmanın gerçek workflow'una göre belirlenmelidir. Aşağıdaki başlıkların tamamı her makalede zorunlu değildir:

- Study design and research questions
- Population, dataset veya sample construction
- Inclusion/exclusion criteria
- Preprocessing
- Proposed method / measurement instrument / model architecture
- Mathematical formulation
- Training veya inference protocol
- Baselines, controls ve ablations
- Evaluation protocol ve endpoints
- Statistical analysis
- Reproducibility, software ve hardware
- Ethics, consent ve governance
- Preregistration ve deviations

### 9.3 Mathematical formulation

Her equation için:

1. Equation'ın amacı prose içinde açıklanmalıdır.
2. Equation numaralandırılmalı ve gerektiğinde referans verilmelidir.
3. Bütün symbols tanımlanmalıdır.
4. Units veya dimensions varsa belirtilmelidir.
5. Assumptions açıkça yazılmalıdır.
6. Bir önceki veya sonraki equation ile ilişki kurulmalıdır.

Definitions, propositions, lemmas ve theorems yalnızca formal olarak gerekli olduğunda kullanılmalıdır. Basit bir kavram sırf teknik görünmesi için `definition` environment içine alınmamalıdır.

### 9.4 Algorithms ve pseudocode

**ZORUNLU (owner directive 2026-08-05).** Her manuscript, prosedürünü **numaralı algorithm
blokları** halinde vermek zorundadır. Bu koşullu bir kural değildir: "yeni bir algorithm
sunulmuyor" gerekçesi bloğu düşürmez, çünkü blok yeniliği değil **yürütme sırasını** belgeler.
Bir okuyucu 16 denklemden hangisinin önce, hangisinin sonra çalıştığını denklem listesinden
çıkaramaz.

En az **iki blok** verilir ve ikisi ayrı ayrı numaralanır:

1. **Üretim / ölçüm prosedürü** — girdiden ham çıktıya kadar ne yapıldığı. Kanıtı üreten
   yürütme budur.
2. **Değerlendirme ve çıkarım prosedürü** — ham çıktıdan raporlanan niceliklere ve karara
   kadar. Bir çalışmanın *öğrenmediği* durumda bile bu blok vardır: tahmin ediciler, aralıklar
   ve karar kuralları bu bloğun adımlarıdır.

Bir çalışma gerçekten tek bir prosedür taşıyorsa, ikinci bloğun neden yokluğu bir eksik değil
de bir özellik olduğu **açıkça yazılır**; sessizce atlanamaz.

Her blok şunları taşımak zorundadır:

- `Input:` ve `Output:` satırları, sembolleriyle ve notation tablosuyla uyumlu,
- initialization,
- numbered steps,
- stopping condition (döngü varsa),
- gerekiyorsa computational complexity,
- **her adımın kullandığı equation'a referansı**. Adım, kullandığı denklemi adıyla göstermek
  zorundadır; "bkz. Bölüm 3" yeterli değildir.

**Adlandırma dürüstlüğü, §0 ile birlikte okunur.** Blok "Algorithm N" olarak numaralanır ve
başlıkta "proposed" kullanılabilir — bu, LaTeX ortamının adıdır, iddianın değil. Ancak
**caption, artefaktın gerçekte ne olduğunu söylemek zorundadır**: bir evaluation instrument,
bir measurement procedure veya bir ablation, "repair algorithm" ya da "proposed framework"
gibi sunulamaz. Örnek biçim: *"The proposed measurement procedure. It is not a repair
algorithm; it is a content-attribution measurement instrument."* Numaralı ortam ile dürüst
caption çelişmez; §0'ın yasakladığı şey, artefaktın **yanlış sınıfta** adlandırılmasıdır.

**Mekanik denetim zorunludur.** Adım–denklem eşlemesi elle korunamaz: bir denklem yeniden
adlandırıldığında adım hiçliği gösterir, bir denklem eklendiğinde hiçbir adıma girmez, ve
ikisi de sessizce çürür. Repository bir gate taşımak zorundadır ve gate şu üçünü de
yakalamalıdır: (a) var olmayan bir label'a referans veren adım, (b) hiçbir adıma girmeyen
denklem, (c) artık tanımlı olmayan bir denklem için bırakılmış exemption. Bir denklemin
*işlem* değil *özellik* olduğu için hiçbir adıma girmemesi meşrudur, ama bu bir exemption
listesinde **gerekçesiyle** yazılır, sessizce tolere edilmez.

Pseudocode, prose içinde zaten açık olan basit workflow'u gereksiz yere tekrar etmemelidir;
ancak bu, yukarıdaki iki bloğu düşürmenin gerekçesi olarak kullanılamaz. Kısıt, blok
**içindeki** gereksiz ayrıntıyadır, blokların varlığına değil.

### 9.5 Tables ve figures

- Ana framework için bir overview figure kullanılabilir.
- Geliştirilen özgün module karmaşıksa ikinci bir detailed figure eklenebilir.
- Dataset, sample, model, hyperparameters, symbols veya constants için table kullanılabilir.
- Her table ve figure metinde ilk kullanımından önce çağrılmalıdır.
- Captions self-contained olmalı; sample, units ve symbols gerektiğinde açıklanmalıdır.

### 9.6 Methods içinde yapılmalı

- Population ve unit of analysis açıkça tanımlanmalıdır.
- Sampling, randomization, seed ve split procedures belirtilmelidir.
- Baselines ve controls operational olarak tanımlanmalıdır.
- “Matched”, “held-out”, “independent”, “frozen”, “random” gibi sıfatların ne anlama geldiği açıklanmalıdır.
- Primary ve secondary endpoints ayrılmalıdır.
- Missing data, exclusions ve failure handling verilmelidir.
- Statistical tests, one/two-sided status, correction procedure ve thresholds yazılmalıdır.
- Data/code/material availability planı belirtilmelidir.
- Deviations ve amendments gizlenmemelidir.

### 9.7 Methods içinde yapılmamalı

- Yöntemin başarılı olduğu ileri sürülmemelidir.
- Result görüldükten sonra seçilen analysis, preregistered gibi sunulmamalıdır.
- Kritik implementation details “standard procedure” denilerek atlanmamalıdır.
- Strict total compute eşitliği yoksa “matched compute” tek başına kullanılmamalı; neyin eşitlendiği açıklanmalıdır.
- Held-out data selection için kullanıldıysa tamamen untouched test set gibi sunulmamalıdır.
- Methods'ta result veya discussion language kullanılmamalıdır.
- Figure ve table, metinde açıklanmadan bırakılmamalıdır.

---

## 10. Results kuralları

Results bölümünün görevi, nerede ve nasıl test yapıldığını kısaca hatırlatmak ve ne elde edildiğini kanıtlarıyla raporlamaktır. “Neden oldu?” sorusu Discussion'a bırakılmalıdır.

### 10.1 Açılış paragrafı

İlk paragrafta kısaca şu bilgiler verilmelidir:

- test edilen model/method/population,
- platform veya execution environment, sonuçları etkiliyorsa,
- datasets veya test sets,
- sample size,
- comparison arms/groups,
- round/trial sayısı,
- primary endpoint,
- scoring procedure.

Bu paragraf Methods'ın tam tekrarı olmamalıdır. Amaç okuyucunun results'u bağımsız takip edebilmesini sağlamaktır.

### 10.2 Deney akışının gösterimi

Test protocol karmaşıksa evaluation schematic verilebilir. Methods'taki framework figure zaten aynı akışı açıkça gösteriyorsa Results'ta duplicate diagram eklenmemelidir. Results figure, workflow değil sonuç pattern'ını göstermelidir.

### 10.3 Analysis sırası

Results, mümkün olduğunca şu sırayı izlemelidir:

1. Run completeness ve data integrity
2. Primary outcomes
3. Secondary outcomes
4. Ablations veya component analyses
5. Robustness/sensitivity analyses
6. Error/failure analyses
7. Audit events veya protocol deviations

Bu sıra preregistration, research questions veya hypotheses ile hizalanmalıdır.

### 10.4 Her ana result için raporlama şablonu

Her comparison için mümkün olduğunca şu bilgiler verilmelidir:

1. Comparison'ın yönü
2. Effect size veya net difference
3. Exact sample size veya counts
4. Confidence interval veya uncertainty
5. Raw ve adjusted $p$-value, gerekiyorsa
6. Heterogeneity veya subgroup direction
7. Tek cümlelik, non-mechanistic sonuç

#### Örnek yapı

> Condition A, Condition B'ye göre daha yüksek accuracy üretmiştir (difference = X, 95\% CI [L, U], adjusted $p=...$). Aynı yön Y subgroup'unun Z'sinde korunmuştur.

### 10.5 Tables ve figures'ın anlatımı

Her display item için metinde:

- neyin gösterildiği,
- ana numerical pattern,
- baseline'a göre difference,
- uncertainty veya variability,
- pre-specified threshold'un karşılanıp karşılanmadığı

kısaca açıklanmalıdır.

Metin table'ın bütün hücrelerini tekrar etmemelidir.

### 10.6 Results içinde yapılmalı

- Exact $n$ değerleri verilmelidir.
- Dataset veya benchmark external ise referanslanmalıdır.
- Primary, secondary ve descriptive analyses etiketlenmelidir.
- Null ve adverse results da raporlanmalıdır.
- Effect size ve uncertainty birlikte sunulmalıdır.
- Figure/table ordering metinle uyumlu olmalıdır.
- Public ve held-out endpoints birbirinden ayrılmalıdır.

### 10.7 Results içinde yapılmamalı

- Causal mechanism açıklanmamalıdır.
- Literature ile uzun karşılaştırma yapılmamalıdır.
- Practical recommendation üretilmemelidir.
- Non-significant result “etki yoktur” diye yazılmamalıdır.
- Pooled tie “equivalence” olarak adlandırılmamalıdır.
- Sadece significant results seçilip null results saklanmamalıdır.
- Aynı result prose, table ve figure içinde gereksiz yere üç kez tekrarlanmamalıdır.
- “Şaşırtıcı”, “dikkat çekici”, “olağanüstü” gibi yorumlayıcı sıfatlar kullanılmamalıdır.

---

## 11. Discussion kuralları

Discussion, sonuçların neden önemli olduğunu, ne anlama gelebileceğini, hangi açıklamalarla uyumlu olduğunu ve hangi sınırlar içinde geçerli olduğunu tartışmalıdır.

### 11.1 Önerilen semantik sıra

#### 1. Ana bulguların kısa sentezi

- Method/design bir veya iki cümlede hatırlatılmalıdır.
- En önemli iki veya üç result kısa biçimde özetlenmelidir.
- Results bölümü yeniden yazılmamalıdır.

#### 2. Interpretation ve olası mechanism

- Result ile interpretation ayrı tutulmalıdır.
- Mechanism doğrudan test edilmediyse “may reflect”, “is consistent with”, “one explanation is” gibi kalıplar kullanılmalıdır.
- Alternative explanations verilmelidir.

#### 3. Prior work ile ilişki

- Bulguların hangi literature line'ı desteklediği, genişlettiği veya sınırladığı açıklanmalıdır.
- Prior work'ün güçlü olduğu ve bu çalışmanın güçlü olduğu yönler dürüst biçimde ayrılmalıdır.
- Multidimensional comparison merkeziyse reference-supported table kullanılabilir.

#### 4. Method'un avantaj ve dezavantajları

- Internal isolation, controls, sample, endpoint ve reproducibility değerlendirilmelidir.
- Model/data quality, assumptions ve protocol choices tartışılmalıdır.
- Method'un kendi içindeki consistency ve residual confounds açıklanmalıdır.

#### 5. Practical implications

- Fayda ve harm birlikte değerlendirilmelidir.
- Recommendation, çalışılan population ve setting ile sınırlandırılmalıdır.
- Average gain, universal rule'a dönüştürülmemelidir.

#### 6. Validity boundaries

- Internal validity
- Construct validity
- Conclusion validity
- External validity
- Statistical power
- Measurement limitations
- Generalization status

ayrı ayrı değerlendirilebilir.

#### 7. Future work

- Mevcut çalışmada kalan en önemli açık sorulara odaklanılmalıdır.
- Future work listesi doğrudan limitation'lardan türetilmelidir.

### 11.2 Discussion içinde yapılmalı

- Results'taki ana rakamlara seçici biçimde atıf yapılmalıdır.
- Her interpretation'ın dayandığı result açık olmalıdır.
- Alternative explanations dürüstçe verilmelidir.
- Advantages ve limitations aynı evidential standard ile tartışılmalıdır.
- Claims, internal isolation ve external generalization bakımından ayrı değerlendirilmelidir.
- Practical implications zarar veya failure cases ile birlikte sunulmalıdır.
- Cümleler çoğunlukla kişisiz olabilir; prior studies aktif attribution ile yazılabilir.

### 11.3 Discussion içinde yapılmamalı

- New results eklenmemelidir.
- Results bölümü sayı sayı tekrarlanmamalıdır.
- Plausible mechanism kanıtlanmış gibi sunulmamalıdır.
- Limitation'lar formalite olarak tek paragrafta geçiştirilmemelidir.
- Bir sensitivity analysis bağımsız replication gibi gösterilmemelidir.
- Comparison table sırf “olması gerektiği” için eklenmemelidir.
- Farazi claims, evidence ile aynı statüde yazılmamalıdır.
- Practical recommendation, scope belirtilmeden verilmemelidir.

---

## 12. Conclusion kuralları

Conclusion kısa, nihai ve yeni bilgi içermeyen bir sentez olmalıdır. Çoğu çalışma için 3--5 paragraf yeterlidir; venue daha kısa isteyebilir.

### 12.1 Önerilen yapı

#### Paragraf 1 — Ne yapıldı?

- Problem ve study design kısaca verilmelidir.
- Hangi comparison veya method ile neyin test edildiği anlatılmalıdır.

#### Paragraf 2 — Ne gösterildi?

- Ana findings bir hikâye halinde sentezlenmelidir.
- Contribution, result ile doğrudan ilişkilendirilmelidir.
- Her headline number tekrar edilmek zorunda değildir.

#### Paragraf 3 — Scope ve practical meaning

- Sonucun hangi population ve setting ile sınırlı olduğu belirtilmelidir.
- En savunulabilir practical veya theoretical implication verilmelidir.

#### Paragraf 4 — Future work

- En yüksek değer taşıyan 2--4 next step verilmelidir.
- Future work, mevcut study'nin eksik control'lerini gizlememelidir.

### 12.2 Conclusion içinde yapılmalı

- Research question'a doğrudan cevap verilmelidir.
- Ana contribution açıkça fakat ölçülü biçimde ifade edilmelidir.
- Scope ve limitation görünür olmalıdır.
- Future directions evidence gaps'ten türetilmelidir.
- Take-home statement present tense ile verilebilir.

### 12.3 Conclusion içinde yapılmamalı

- Yeni citation eklenmemelidir, venue özel olarak gerektirmedikçe.
- Yeni analysis, sayı, dataset veya claim eklenmemelidir.
- Abstract'tan daha güçlü bir sonuç kurulmamaldır.
- Discussion'ın tamamı tekrar edilmemelidir.
- “Bu çalışma alanı değiştirecektir” gibi spekülatif cümleler kullanılmamalıdır.
- General law, tek sample veya limited benchmark'tan çıkarılmamalıdır.

---

## 13. Contribution ve originality'nin kurulması

Contribution yalnızca “new”, “novel” veya “first” ifadeleriyle kurulmaz. Her contribution aşağıdaki matrise bağlanmalıdır:

| Unsur | Soru |
|---|---|
| Problem | Önceki çalışmalarda hangi bilimsel veya operational problem çözülmemiştir? |
| Gap | Hangi ingredient, confound, population veya baseline eksiktir? |
| Response | Bu çalışmada hangi method, control veya analysis sunulmaktadır? |
| Evidence | Hangi result bu contribution'ı desteklemektedir? |
| Boundary | Bu contribution hangi scope ile sınırlıdır? |

### Contribution türleri ayrılmalıdır

- **Methodological contribution:** Yeni method, instrument, framework veya protocol
- **Empirical contribution:** Yeni result veya regularity
- **Theoretical contribution:** Yeni explanation, formalization veya conceptual distinction
- **Evaluation contribution:** Yeni benchmark, control, baseline veya audit design
- **Practical contribution:** Uygulanabilir procedure veya decision rule
- **Reproducibility contribution:** Code, data, preregistration, audit veya artifact

### Yapılmalı

- Contribution listesi birbirinden bağımsız maddeler içermelidir.
- Her contribution bir result veya artifact ile doğrulanmalıdır.
- “İlk” iddiası kullanılacaksa systematic, current search ile desteklenmelidir.
- Strongest claim, strongest controlled comparison'a dayanmalıdır.

### Yapılmamalı

- Aynı contribution farklı sözcüklerle üç kez sayılmamalıdır.
- Yalnızca farklı dataset kullanılması temel novelty olarak sunulmamalıdır.
- Yapılmamış ablation veya replication contribution gibi yazılmamalıdır.
- Methodological contribution ile empirical finding karıştırılmamalıdır.
- Disjoint sensitivity result generalization proof olarak sunulmamalıdır.

---

## 14. Literature ve citation kuralları

### 14.1 Literature synthesis

Literature aşağıdaki eksenlerde gruplanmalıdır:

- method family,
- task/domain,
- model/population,
- positive vs negative evidence,
- compute regime,
- evaluation design,
- known confounds,
- remaining gap.

#### Yapılmalı

- Primary evidence, claim'in doğrudan dayanağı olarak tercih edilmelidir.
- Review ve systematic review, alanın sentezi için kullanılmalıdır.
- Contradictory findings dengeli biçimde sunulmalıdır.
- Citation, desteklediği cümleye mümkün olduğunca yakın verilmelidir.
- Güncel ve authoritative sources kontrol edilmelidir.
- Study-type reporting guidelines kullanılmalıdır.

#### Yapılmamalı

- Citation dumping yapılmamalıdır.
- Bir review, primary experiment'ın doğrudan sonucu gibi sunulmamalıdır.
- Kaynakta bulunmayan sayı veya conclusion kaynağa atfedilmemelidir.
- Predatory veya güvenilmez journals kullanılmamalıdır.
- Sırf citation count yüksek olduğu için eski ve alakasız kaynak seçilmemelidir.
- “No prior study” ifadesi yeterli search olmadan kullanılmamalıdır.

### 14.2 Citation tense

- Belirli bir study'nin yaptığı işlem: past simple.
- Alan genelindeki devam eden trend: present perfect.
- Hâlen kabul edilen teori veya definition: present simple.

---

## 15. Statistical ve evidential reporting

### 15.1 Temel ayrımlar

- Non-significance **etki yokluğu değildir**.
- No observed difference **equivalence değildir**.
- Pooled tie **unit-level equality değildir**.
- Direction consistency **magnitude replication değildir**.
- Fresh seeds **independent population replication değildir**.
- Statistical significance **practical importance değildir**.
- Association **causation değildir**.
- Strong prediction **mechanism proof değildir**.

### 15.2 Raporlanması gerekenler

- Exact $n$
- Unit of analysis
- Effect size
- Confidence interval veya uncertainty
- Exact $p$-value, uygunsa
- Multiple-testing correction
- One-sided/two-sided status
- Primary/secondary/descriptive classification
- Missing data ve exclusions
- Randomization/seeds
- Heterogeneity ve subgroup rules
- Preregistration status
- Deviations ve amendments

### 15.3 Claim calibration

| Evidence level | Uygun ifade |
|---|---|
| Descriptive | “X gözlenmiştir.” |
| Association | “X, Y ile ilişkilidir.” |
| Controlled attribution | “A ve B sabit tutulduğunda C bileşenine bağlı difference gözlenmiştir.” |
| Causal effect | Uygun intervention ve confound control varsa “X, Y üzerinde causal effect üretmiştir.” |
| Mechanism | Competing mechanisms doğrudan ayrıştırılmışsa kullanılmalıdır. |
| General law | Multiple independent settings ve replications gerektirir. |

### 15.4 Yapılmamalı

- Sadece $p$-value verilmemelidir.
- $p>0.05$ için “eşittir” veya “etkisizdir” denmemelidir.
- Underpowered null result refutation olarak sunulmamalıdır.
- Post hoc subgroup confirmatory gibi yazılmamalıdır.
- Multiple comparisons correction olmadan family-level claim kurulmamaldır.
- Confidence interval verilmeden precision iddiası yapılmamalıdır.
- Average improvement universal benefit'e dönüştürülmemelidir.

---

## 16. Computational, ML ve software studies için ek kurallar

Bu alanlarda aşağıdaki bilgiler sonuçların yorumlanması ve replication için kritik olabilir:

- Exact model name ve checkpoint
- Model version/digest
- Dataset version ve split
- Prompt templates
- Decoding parameters
- Seed construction
- Number of samples/rounds
- Hardware ve software versions, sonuç veya runtime etkileniyorsa
- Context length ve token limits
- Baselines ve compute definition
- Training vs inference distinction
- Code execution sandbox
- Evaluation harness
- Public vs hidden tests
- Data leakage checks
- Model/data contamination risk
- Cost ve wall-clock metrics, claim için relevant ise
- Code, logs ve artifact availability

### Yapılmalı

- “Matched compute” tam olarak operationalize edilmelidir.
- Output-sample equality ile total FLOPs equality karıştırılmamalıdır.
- Model family veya API version değişebilir olduğu için exact version kaydedilmelidir.
- Benchmark contamination ve test leakage riskleri tartışılmalıdır.
- LLM-as-judge kullanılıyorsa judge model, prompt, calibration ve agreement verilmelidir.
- Human evaluation varsa annotator training, blinding, rubric ve agreement raporlanmalıdır.

### Yapılmamalı

- “Same model” denilip version/checkpoint belirtilmeden bırakılmamalıdır.
- Seed verildiği için determinism garanti edilmiş gibi yazılmamalıdır.
- Public benchmark success real-world deployment readiness olarak sunulmamalıdır.
- Hidden tests sample selection'da kullanıldıysa untouched gibi adlandırılmamalıdır.
- Model output collision data reuse kanıtı olarak otomatik yorumlanmamalıdır; provenance kontrol edilmelidir.

---

## 17. Figures, tables ve equations

### 17.1 Figures

- Figure, metinde ilk kez anılmadan önce yerleştirilmemelidir.
- Figures ascending order ile çağrılmalıdır.
- Caption concise title ile başlamalı ve figure'ın anlaşılması için gerekli details'i vermelidir.
- Figure mümkün olduğunca ana metinden bağımsız anlaşılabilir olmalıdır.
- Axes, units, error bars, sample sizes ve statistical annotations açıklanmalıdır.
- Accessible colors ve distinguishable markers kullanılmalıdır.
- Aynı data gereksiz biçimde hem table hem figure olarak verilmemelidir.

#### Figure işlevleri

- Methods figure: workflow, architecture veya study design
- Results figure: effect, trend, uncertainty, comparison veya failure pattern
- Discussion figure: yalnızca conceptual synthesis gerçekten gerekli ise

#### Yapılmamalı

- Caption içine uzun Discussion yazılmamalıdır.
- Figure'da görünmeyen causal conclusion caption'a eklenmemelidir.
- Renk tek başına bilgi taşıyan unsur olmamalıdır.
- Düşük resolution veya okunmayan label kullanılmamalıdır.
- Results'taki figure Methods workflow'unu gereksiz yere tekrar etmemelidir.

### 17.2 Tables

- Table title kısa ve descriptive olmalıdır.
- Units, abbreviations ve statistical markers footnotes'ta açıklanmalıdır.
- Decimal precision tutarlı olmalıdır.
- Sample size ve endpoint açık olmalıdır.
- Table ana metni desteklemeli, onun yerine geçmemelidir.

#### Yapılmamalı

- Table içeriği prose içinde satır satır tekrar edilmemelidir.
- Farklı denominator'lar açıkça belirtilmeden aynı column'da karıştırılmamalıdır.
- Significant sonuçlar yalnızca bold ile seçilerek cherry-picking yapılmamalıdır.
- Screenshot olarak table eklenmemelidir.

### 17.3 Equations

- Equation prose tarafından tanıtılmalıdır.
- Her symbol tanımlanmalıdır.
- Equation punctuation cümle yapısına uygun olmalıdır.
- Equation'ın scientific purpose'u açıklanmalıdır.
- Numbering ve cross-reference tutarlı olmalıdır.

#### Yapılmamalı

- Equation image olarak eklenmemelidir.
- Sırf teknik görünüm için gereksiz equation kullanılmamalıdır.
- Unused variables bırakılmamalıdır.
- Sign, inequality direction veya subscript editing sırasında değiştirilmemelidir.

---

## 18. End matter ve disclosure sections

Aşağıdaki sections venue ve study type'a göre değerlendirilmelidir:

### Acknowledgements

- Authorship criteria karşılamayan katkılar belirtilmelidir.
- Kısa ve somut olmalıdır.
- Effusive praise, reviewer/editor teşekkürleri ve belirsiz ifadeler kullanılmamalıdır.

### Funding

- Funder names ve grant numbers doğru verilmelidir.
- Funder'ın study design, analysis veya publication üzerindeki rolü venue isterse açıklanmalıdır.

### Author Contributions

- Her author'ın contribution'ı açıkça belirtilmelidir.
- CRediT taxonomy kullanılabilir.
- Contribution statement, authorship criteria'nın yerine geçmez.

### Competing Interests / Conflict of Interest

- Financial ve non-financial interests açıkça beyan edilmelidir.
- Conflict yoksa bunun da açık statement ile belirtilmesi gerekebilir.

### Ethics ve Consent

- Human/animal research için committee, approval identifier, relevant standards ve consent bilgisi verilmelidir.
- Identifiable participant information için publication consent ayrıca ele alınmalıdır.

### Data Availability

- Minimum dataset'in nerede, hangi koşulla ve hangi identifier ile erişilebilir olduğu belirtilmelidir.
- “Available upon reasonable request” kullanılıyorsa neden ve access conditions açıklanmalıdır.

### Code Availability

- Code repository, version/tag, license ve execution instructions verilebilir.
- Proprietary code varsa restriction açıkça belirtilmelidir.

### Preregistration ve Protocol

- Registry, timestamp, identifier ve deviations açıklanmalıdır.
- Internal version-control timestamp, third-party registry ile eşdeğer gösterilmemelidir.

### Supplementary Information ve Appendix

- Main argument için zorunlu olan content supplement'e itilmemelidir.
- Reproducibility details, extended tables, proofs, additional analyses ve materials burada verilebilir.
- Venue appendix yerine supplementary file istiyorsa bu yapı izlenmelidir.

### AI-assisted writing declaration

- Venue veya institutional policy gerektiriyorsa AI tool kullanımının kapsamı açıklanmalıdır.
- Scientific accuracy, citation verification ve authorship responsibility insan authors'a aittir.

---

## 19. Bölümler arası semantik tutarlılık

Makale bir **promise-delivery chain** olarak kontrol edilmelidir:

| Bölüm | İşlev |
|---|---|
| Introduction | Hangi sorunun neden test edilmesi gerektiğini vaat eder. |
| Methods | Bu sorunun nasıl test edildiğini gösterir. |
| Results | Testin ne ürettiğini bildirir. |
| Discussion | Result'ın ne anlama geldiğini ve ne anlama gelmediğini açıklar. |
| Conclusion | Research question'a en savunulabilir cevabı verir. |

### Single source of truth tablosu tutulmalıdır

En az şu alanlar tek bir consistency sheet içinde kaydedilmelidir:

- Research question
- Hypotheses
- Population ve sample sizes
- Conditions/arms/groups
- Inclusion/exclusion counts
- Primary ve secondary endpoints
- Baselines
- Model/dataset versions
- Exact effect sizes
- Confidence intervals
- $p$-values ve corrections
- Tables/figures
- Preregistration status
- Limitations
- Contribution wording

### Cross-section audit soruları

- Abstract'taki her sayı Results'ta var mı?
- Introduction'daki her major promise Methods'ta test edilmiş mi?
- Methods'taki her primary analysis Results'ta raporlanmış mı?
- Discussion'daki her interpretation belirli bir result'a bağlı mı?
- Conclusion, Abstract'tan daha güçlü mü?
- Aynı sample farklı bölümlerde farklı adla mı kullanılmış?
- Baseline yönü değişmiş mi?
- “Replication”, “sensitivity” veya “validation” statüsü kaymış mı?

### Yapılmamalı

- Number drift
- Terminology drift
- Baseline switching
- Endpoint switching
- Sample-status switching
- Discovery-confirmation mixing
- Result-discussion contamination
- Conclusion inflation

---

## 20. LaTeX güvenlik kuralları

LaTeX metni düzenlenirken aşağıdaki öğeler korunmalıdır:

- `\section`, `\subsection`, `\paragraph`
- `\label`, `\ref`, `\eqref`, `\S\ref`
- `\citep`, `\citet`
- `\begin{...}` / `\end{...}` pairs
- `table`, `figure`, `equation`, `align`, `enumerate`, `itemize`
- Custom macros
- Mathematical symbols ve operators
- `\input{...}` ve file paths
- Placement specifiers `[t]`, `[h]`, vb.
- Width settings
- Escape characters: `\%`, `\_`, `\&`, `\#`
- Dashes: `--`, `---`

### Yapılmalı

- Environment balance kontrol edilmelidir.
- Duplicate labels aranmalıdır.
- Undefined refs ve citations tespit edilmelidir.
- Equation punctuation ve surrounding prose kontrol edilmelidir.
- Tables ve figures ilk callout sırasına göre doğrulanmalıdır.
- Custom macros anlamı bilinmeden değiştirilmemelidir.

### Yapılmamalı

- Equation içindeki number, sign veya inequality yönü dil editing sırasında değiştirilmemelidir.
- `\citep` ve `\citet` rastgele dönüştürülmemelidir.
- Table/figure environments kaldırılmamalıdır.
- Macro isimleri stil amacıyla yeniden adlandırılmamalıdır.
- `%` ve `_` gibi special characters kaçışsız bırakılmamalıdır.
- Author'ın bilinçli technical English terms'i LaTeX hatası sanılarak değiştirilmemelidir.

---

## 21. Kesinlikle yapılmaması gerekenler

1. Veri veya citation uydurmak
2. Missing method detail tahmin etmek
3. Significant olmayan sonucu “no effect” diye yazmak
4. Pooled tie'ı equivalence olarak sunmak
5. Association'dan causality çıkarmak
6. Behavioral result'tan internal mechanism kanıtlamak
7. Tek benchmark'tan general law çıkarmak
8. Abstract'ta ana metinden güçlü claim kullanmak
9. Conclusion'da yeni result eklemek
10. Results'ta neden/mechanism açıklamak
11. Methods'ta method'un başarılı olduğunu savunmak
12. Discussion'da unreported analysis sunmak
13. Same concept için farklı terms kullanmak
14. Same quantity için farklı numbers vermek
15. Baseline'ı bölümden bölüme değiştirmek
16. Sensitivity sample'ı independent replication olarak adlandırmak
17. Discovery data'yı confirmatory evidence'a karıştırmak
18. “First”, “only”, “unprecedented” iddiasını search olmadan kullanmak
19. Prior work'ü novelty için yanlış temsil etmek
20. Citation dumping yapmak
21. Her cümleyi passive yaparak doğal dili bozmak
22. Tense'leri retorik işlevden bağımsız seçmek
23. Aşırı heading ile story'yi parçalamak
24. Her result'ı abstract, introduction, discussion ve conclusion'da aynı ayrıntıyla tekrar etmek
25. Limitation'ları küçümsemek veya sonuçtan kopuk vermek
26. Statistical significance'ı practical importance ile eşitlemek
27. Average benefit'i uniform safety olarak yazmak
28. Figure/table caption'ı ana metinle çeliştirmek
29. Equation veya LaTeX structure bozmak
30. Venue-specific instructions'ı görmezden gelmek

---

## 22. Düzenleme iş akışı

Bir metin tek aşamada “daha akademik” hale getirilmemelidir. Aşağıdaki aşamalar izlenmelidir.

### Aşama 1 — Venue ve study-type kontrolü

- Target journal belirlenir.
- Article type belirlenir.
- Word, figure, abstract ve section limits çıkarılır.
- Uygun reporting guideline seçilir.

### Aşama 2 — Scientific skeleton çıkarımı

- Research question
- Hypotheses
- Design
- Population/sample
- Conditions
- Endpoints
- Main results
- Limitations
- Contributions

tek sayfalık bir özet halinde çıkarılır.

### Aşama 3 — Consistency sheet

Bütün numbers, terms, models, datasets, symbols ve claims tek bir source-of-truth tablosuna yazılır.

### Aşama 4 — Promise-delivery audit

Introduction promises, Methods tests, Results answers, Discussion interpretations ve Conclusion claims eşleştirilir.

### Aşama 5 — Section-level restructuring

Her bölüm kendi epistemik görevine göre yeniden sıralanır. Fazla alt başlıklar ve tekrarlar kaldırılır.

### Aşama 6 — Claim audit

Her claim için şu sorular sorulur:

- Hangi result destekliyor?
- Confirmatory mi descriptive mi?
- Causal language uygun mu?
- Hangi confounds açık?
- Hangi scope ile sınırlı?

### Aşama 7 — Language editing

- Passive/active balance düzeltilir.
- Tense matrix uygulanır.
- Long sentences bölünür.
- Abartı ve metadiscourse çıkarılır.
- Transitions güçlendirilir.

### Aşama 8 — Citation ve evidence audit

- Her factual claim'in source'u kontrol edilir.
- Primary vs review sources ayrılır.
- Unsupported novelty claims kaldırılır.

### Aşama 9 — Technical/LaTeX audit

- Environments
- Labels/refs
- Citations
- Equations
- Tables/figures
- Macros
- Escaped characters

kontrol edilir.

### Aşama 10 — Reverse reading

Makale Conclusion'dan Abstract'a doğru geriye okunur. Bu, claim inflation ve promise-delivery mismatches'ı ortaya çıkarır.

---

## 23. Son kontrol listesi

### Scientific integrity

- [ ] Research question tek ve açık mı?
- [ ] Her headline claim bir result'a bağlı mı?
- [ ] Causal language design'a uygun mu?
- [ ] Null, tie ve equivalence doğru ayrılmış mı?
- [ ] Descriptive ve confirmatory analyses ayrılmış mı?
- [ ] Limitations claims'i gerçekten daraltıyor mu?

### Story

- [ ] Introduction genelden özele ilerliyor mu?
- [ ] Her paragraf bir sonrakini hazırlıyor mu?
- [ ] Gap test edilebilir mi?
- [ ] Current study gap'e doğrudan cevap veriyor mu?
- [ ] Contribution bir cümlede ifade edilebiliyor mu?

### Section coherence

- [ ] Abstract, Results ve Conclusion aynı ana sonucu mu söylüyor?
- [ ] Methods'taki her primary test Results'ta var mı?
- [ ] Discussion'daki her interpretation Results'a bağlı mı?
- [ ] Conclusion yeni bilgi içeriyor mu?
- [ ] Sample, baseline ve endpoint adları tutarlı mı?

### Language

- [ ] Tense retorik işleve uygun mu?
- [ ] Passive voice doğal mı?
- [ ] Long sentences azaltılmış mı?
- [ ] Abartılı sıfatlar çıkarılmış mı?
- [ ] Acronyms doğru yerde tanımlanmış mı?
- [ ] Bilerek English bırakılan terms korunmuş mu?

### Methods and reproducibility

- [ ] Population, sample ve unit of analysis açık mı?
- [ ] Baselines ve controls operational olarak tanımlı mı?
- [ ] Seeds/randomization/splits verilmiş mi?
- [ ] Statistical plan yeterli mi?
- [ ] Deviations ve amendments raporlanmış mı?
- [ ] Data/code availability açık mı?

### Figures, tables and equations

- [ ] Her display item metinde çağrılıyor mu?
- [ ] Captions kendi başına anlaşılır mı?
- [ ] Exact $n$, units ve symbols tanımlı mı?
- [ ] Prose ile table/figure numbers uyumlu mu?
- [ ] Equations'daki symbols ve assumptions açıklanmış mı?

### LaTeX

- [ ] Bütün `\begin`/`\end` pairs dengeli mi?
- [ ] Labels unique mi?
- [ ] Refs ve citations tanımlı mı?
- [ ] Custom macros korunmuş mu?
- [ ] Mathematical signs değişmemiş mi?

---

## 24. Bir LLM veya editöre verilebilecek bağlayıcı talimat

> Bu makaleyi yalnızca dil bakımından değil, bilimsel argüman, bölüm işlevi ve bölümler arası tutarlılık bakımından düzenle. Önce target venue ve study type'a uygun reporting rules'u belirle. Research question, hypotheses, design, population, sample, conditions, endpoints, primary results, limitations ve contributions için bir source-of-truth çıkar. Abstract, Introduction, Methods, Results, Discussion ve Conclusion arasında promise-delivery chain kur. Introduction'ı genelden özele ilerleyen problem → prior work → unresolved gap → current study → contributions → scope zinciriyle düzenle. Methods'ı reproducible ve result-independent yaz; equations, symbols, assumptions, figures, algorithms ve parameters'ı açıkla. Results'ın ilk paragrafında testlerin nerede ve nasıl yapıldığını kısaca özetle; ardından primary, secondary ve robustness analyses'i önceden belirlenen sırayla, effect size ve uncertainty ile raporla. Results'ta neden veya mechanism tartışma. Discussion'da result, interpretation, prior work, alternatives, practical implications ve validity boundaries'yi birbirinden ayır. Conclusion'da yeni bilgi ekleme; ne yapıldığını, ne gösterildiğini, scope'u ve en önemli future directions'ı kısa biçimde sentezle. Akademik, kişisiz ve ölçülü ton kullan; passive voice'u özellikle process odaklı cümlelerde tercih et, ancak faili gizleyen veya yapay passive structures kurma. Tense'i retorik işleve göre seç: general knowledge present, prior studies past/present perfect, performed methods and observed results past, current implications present. Non-significant result'ı no effect, pooled tie'ı equivalence, association'ı causation veya plausible explanation'ı mechanism olarak yazma. Unsupported novelty, citation, number veya method detail uydurma. Bilerek İngilizce bırakılan technical terms'i değiştirme. LaTeX commands, citations, labels, refs, macros, equations, tables, figures ve environments'ı aynen koru. Yapılan substantive düzeltmeleri ve çözülemeyen contradictions'ı ayrıca raporla.

---

## 25. Dayanak alınan genel standartlar

Bu kural seti, aşağıdaki official writing ve reporting kaynaklarıyla uyumlu biçimde hazırlanmıştır:

- [APA Style: Verb Tense](https://apastyle.apa.org/style-grammar-guidelines/grammar/verb-tense)
- [Nature: Initial Submission and Manuscript Structure](https://www.nature.com/nature/for-authors/initial-submission)
- [Scientific Reports: Submission Guidelines](https://www.nature.com/srep/author-instructions/submission-guidelines)
- [PLOS ONE: Submission Guidelines](https://journals.plos.org/plosone/s/submission-guidelines)
- [ICMJE Recommendations](https://www.icmje.org/recommendations/)
- [EQUATOR Network Reporting Guidelines](https://www.equator-network.org/)
- [CRediT Contributor Role Taxonomy](https://credit.niso.org/)

Bu kaynaklar genel çerçeveyi sağlar; her submission öncesinde hedef derginin güncel kuralları ayrıca kontrol edilmelidir.
