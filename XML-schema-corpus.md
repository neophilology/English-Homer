# Corpus XML Schema
# Corpus XML Schema
## A Custom Minimal Structure Based on TEI

The Homer Living Network project incorporates multiple translations with XML structure. The schema follows guidelines from TEI 2.0 in a minimal implementation that will be gradually expanded throughout the project. An updated list of structured translations will be regularly published here.

### Translations Included in the First Phase of the Study

| Title    | Text | Author                          | Year | Period        | Span    | Verse | Publisher                    | Edition | Source   | Language | Country | Reception |
|----------|------|----------------------------------|------|---------------|---------|-------|------------------------------|---------|----------|----------|---------|-----------|
| Odyssey  | 1    | Georges Chapman                 | 1615 | Renaissance   | <1700   | TRUE  | First                        | Gutemberg | English  | England  | Positive |
| Odyssey  | 0    | John Ogilby                     | 1665 | Renaissance   | <1700   |       |                              |         |          |          |         |
| Odyssey  | 0    | Thomas Hobbes                   | 1675 | Renaissance   | <1700   |       |                              |         |          |          |         |
| Odyssey  | 1    | Alexander Pope                  | 1725 | Enlightenment | <1820   |       |                              |         |          |          |         |
| Odyssey  | 1    | William Cowper                  | 1791 | Enlightenment | <1820   |       |                              |         |          |          |         |
| Odyssey  | 0    | H.F. Cary                       | 1823 | Enlightenment | <1820   |       |                              |         |          |          |         |
| Odyssey  | 0    | William Sotheby                 | 1834 | Enlightenment | <1820   |       |                              |         |          |          |         |
| Odyssey  | 0    | Theodore Alois Buckley          | 1851 | Victorian     | <1900   |       |                              |         |          |          |         |
| Odyssey  | 1    | P. S. Worsley                   | 1861 | Victorian     | <1900   | TRUE  | Edinburgh, W. Blackwood & Sons | First    | English  | England  | Positive |
| Odyssey  | 0    | Dr. Giles                       | 1861 | Victorian     | <1900   |       |                              |         |          |          |         |
| Odyssey  | 0    | Thomas Starling Norgate         | 1862 | Victorian     | <1900   |       |                              |         |          |          |         |
| Odyssey  | 1    | William Cullen Bryant           | 1871 | Victorian     | <1900   |       |                              |         |          |          |         |
| Odyssey  | 1    | Samuel Henry Butcher / Andrew Lang | 1879 | Victorian  | <1900   |       |                              |         |          |          |         |
| Odyssey  | 0    | George Herbert Palmer           | 1886 | Victorian     | <1900   |       |                              |         |          |          |         |
| Odyssey  | 0    | Willliam Morris                 | 1887 | Victorian     | <1900   |       |                              |         |          |          |         |
| Odyssey  | 0    | Samuel Butler                   | 1900 | Modernist     | <1970   |       |                              |         |          |          |         |
| Odyssey  | 0    | Henry Bernard Cotterill         | 1911 | Modernist     | <1970   |       |                              |         |          |          |         |
| Odyssey  | 0    | Augustus Taber Murray           | 1919 | Modernist     | <1970   |       |                              |         |          |          |         |
| Odyssey  | 0    | T.E. Lawrence                   | 1932 | Modernist     | <1970   |       |                              |         |          |          |         |
| Odyssey  | 0    | E.V. Rieu                       | 1945 | Modernist     | <1970   |       |                              |         |          |          |         |
| Odyssey  | 1    | Robert Fitzgerald               | 1961 | Modernist     | <1970   |       |                              |         |          |          |         |
| Odyssey  | 0    | Richmond Lattimore              | 1965 | Modernist     | <1970   |       |                              |         |          |          |         |
| Odyssey  | 0    | Walter Shawring                 | 1980 | Modernist     | <1970   | prose |                              |         |          |          |         |
| Odyssey  | 0    | Allen Mandelbaum                | 1990 | Contemporary  | >1971   | blank verse |                        |         |          |          |         |
| Odyssey  | 0    | Brian Kemball-Cook              | 1993 | Contemporary  | >1971   |       |                              |         |          |          |         |
| Odyssey  | 1    | Robert Fagles                   | 1996 | Contemporary  | >1971   |       |                              |         |          |          |         |
| Odyssey  | 0    | Stanley Lombardo                | 2000 | Contemporary  | >1971   | verse |                              |         |          |          |         |
| Odyssey  | 1    | Emily Wilson                    | 2017 | Contemporary  | >1971   |       |                              |         |          |          |         |
| Odyssey  | 0    | Peter Green                     | 2018 | Contemporary  | >1971   |       |                              |         |          |          |         |
| Odyssey  | 0    |                                  |      | Contemporary  | >1971   |       |                              |         |          |          |         |

### The XML Minimal Schema

The schema includes:
- Bibliographical data
- Characters and epithets
- Books 1-24 (chapters)
- Significant episodes

#### Examples:

**Bibliographical:**
```xml
<TEI>
  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>The Odyssey</title>
        <translator>Translator Name</translator>
      </titleStmt>
      <publicationStmt>
        <publisher>Publisher</publisher>
        <date>Year</date>
      </publicationStmt>
    </fileDesc>
  </teiHeader>
  <text>
    <body>
      <!-- Content here -->
    </body>
  </text>
</TEI>
```

**Books:**
```xml
<div type="book" n="1">
  <head>Book 1</head>
  <p>Text content...</p>
</div>
```

**Character's epithets:**
```xml
<seg type="epithet" character="athena">grey-eyed Athena</seg>
<seg type="metaphor" subtype="sea">like waves breaking on a distant shore</seg>
<placeName>Ithaca</placeName>
<persName>Penelope</persName>
```

**Episodes:**
```xml
<div type="episode" n="1">
  <head>Odysseus Meets Nausicaa</head>
  <speaker>Odysseus</speaker>
  <listPerson>
    <person>Odysseus</person>
    <person>Nausicaa</person>
  </listPerson>
  <note type="subject">First encounter and supplication</note>
  <milestone unit="book" n="6"/>
  <milestone unit="line" n="85-315" ed="Greek"/>
  <p>Text of the episode...</p>
</div>
```