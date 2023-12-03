# Dataset Info

**Name** <p>multilingual task-oriented data</p>

**Data** <p>Cross lingual text data between English, Spanish and Thai. The domains present in the dataset are Weather (information about the weather), Alarm (set an alarm or do an action based on specified conditions) and Reminder (remind something on a specific time)</p>

**Download location** <p>https://fb.me/multilingual_task_oriented_data</p>

**Data collection** <p>In the first step of data accumulation 43000 English utterances were collected across the three listed domains, by asking native English speakers to produce utterances for each intent, the way they would ask an English conversational agent. </p> <p>Following the collection of the English utterances, two annotators would label the intent and spans that correspond to the slots for each utterance. If a disagreement arose, a third annotator would resolve the difference.</p><p>The next step was to collect the Spanish and Thai data, where native speakers of each language would translate a sample of the collected English utterances. For Spanish the same annotation procedure as English was followed, where the third annotator was a bilingual English/Spanish speaker, but for Thai as there was no bilingual speaker available, meaning that they had to throw out all utterances where the two annotators couldn’t come to the same conclusion.</p><p>In the end the Spanish and Thai portion of the dataset was upscaled to reach the same number of English samples.
<p>The main use for this dataset is to facilitate the creation of conversational models in low-resource countries through cross lingual transfer learning.</p>

**Annotation** <p>As mentioned above the annotation present, is an annotation of the slots for each intent of each domain, through the use of human annotators. The annotation is following a BIO format as used in NER.

**Format** <p>The dataset is stored in TSV and CONLLU files. Each line of each file contains the raw text, the tokenized text, some information about the tokenization, the language of the text, the character span of the tokens corresponding to each slot and the intent.

**Licence** <p>CC-BY-SA, which is the Creative Commons Attribution-ShareAlike. Which stipulates that the work can be used freely as long as appropriate credit is given to the original dataset creators and that any work based on this dataset needs to be shared with the same license.

# Stats
<p>As mentioned above, this dataset isn’t a conversational dataset between two sides, rather it contains the utterances of a user towards a system and it classifies their intent and the corresponding slots. Meaning that there are no turns to count or extract stats for (1 turn per sample), for the same reasons there’s no dialogues (1 utterance and dialogue per sample). So the following dataset exploration will contain all expected stats per language and for the whole, as long as the unique intents measured.</p>

| language | Vocab | unique intent count | dialogue count | turn count | word count | word mean | word std | sentence count | sentence mean | sentence std |
|----------|-------|---------------------|----------------|------------|------------|-----------|----------|----------------|---------------|--------------|
| English  | 4110  | 12                  | 30521          | 30521      | 221009     | 7.25      | 2.50     | 30580          | 1.001         | 0.044        |
| Spanish  | 1974  | 12                  | 28936          | 28936      | 209512     | 7.24      | 2.75     | 28968          | 1.001         | 0.033        |
| Thai     | 2101  | 10                  | 28028          | 28028      | 45422      | 1.62      | 0.96     | 28184          | 1.005         | 0.080        | 
| Sum      | 7600  | 12                  | 87485          | 87485      | 475943     | 5.55      | 3.46     | 87732          | 1.002         | 0.005        | 

<p>For the stats above each utterance was split into sentences and tokens for the calculations.</p>

# Discussion
<p>The data doesn’t look natural, since it’s comprised by one-way user utterances towards a system, with the Spanish and Thai utterances being a result of translation, making the naturality suffer even more. That being the case, the data has the exact format that can be used to easily train the intent recognition model of a conversational agent for a low-resource language, especially when extending a base model from the English language to work for the target languages.</p><p>The limitations of this dataset are the low number of samples for the target languages, since it’s very expensive and slow to create a quality human translation. To mitigate this issue the researchers upsampled both the Spanish and Thai part of the datasets, by duplicating samples randomly. This brought the languages to an adequate level for training, but sacrificed data quality.</p>


