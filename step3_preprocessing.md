## الخطوة 3 (الجزء 1): تجهيز ومعالجة البيانات لتدريب GAN

في هذه المرحلة، قمنا بتجهيز بيانات مجموعة "Predict Students' Dropout and Academic Success" لتكون مناسبة لتدريب نماذج الشبكات العصبية التوليدية التنافسية (GANs). الهدف هو تحويل البيانات الأولية إلى تنسيق رقمي موحد يمكن لنماذج GAN التعامل معه بفعالية.

### الخطوات المتبعة:

1.  **تحميل البيانات:** تم تحميل مجموعة البيانات من ملف `data.csv`.
2.  **تحديد أنواع الميزات:** تم فصل الميزات إلى فئوية (Categorical) ورقمية (Numerical) بناءً على طبيعة البيانات الموضحة في وثائق المجموعة أو من خلال الفحص المباشر. تم التعامل مع 36 ميزة إجمالاً (باستثناء العمود المستهدف 'Target').
    *   **الميزات الرقمية (19):** ['Application order', 'Previous qualification (grade)', 'Admission grade', 'Age at enrollment', 'Curricular units 1st sem (credited)', 'Curricular units 1st sem (enrolled)', 'Curricular units 1st sem (evaluations)', 'Curricular units 1st sem (approved)', 'Curricular units 1st sem (grade)', 'Curricular units 1st sem (without evaluations)', 'Curricular units 2nd sem (credited)', 'Curricular units 2nd sem (enrolled)', 'Curricular units 2nd sem (evaluations)', 'Curricular units 2nd sem (approved)', 'Curricular units 2nd sem (grade)', 'Curricular units 2nd sem (without evaluations)', 'Unemployment rate', 'Inflation rate', 'GDP']
    *   **الميزات الفئوية (17):** ['Marital status', 'Application mode', 'Course', 'Daytime/evening attendance\t', 'Previous qualification', 'Nacionality', "Mother's qualification", "Father's qualification", "Mother's occupation", "Father's occupation", 'Displaced', 'Educational special needs', 'Debtor', 'Tuition fees up to date', 'Gender', 'Scholarship holder', 'International']
3.  **معالجة الميزات الرقمية:** تم تطبيق تحجيم Min-Max (MinMaxScaler) على جميع الميزات الرقمية لتحويل قيمها إلى النطاق [0, 1]. هذا يساعد على استقرار تدريب نماذج الشبكات العصبية.
4.  **معالجة الميزات الفئوية:** تم تطبيق ترميز One-Hot (OneHotEncoder) على جميع الميزات الفئوية. يقوم هذا بتحويل كل فئة إلى عمود ثنائي جديد (0 أو 1)، مما يسمح للنماذج بالتعامل معها كميزات رقمية. تم ضبط المعالج لتجاهل الفئات غير المعروفة التي قد تظهر في بيانات الاختبار (على الرغم من أننا نركز على بيانات التدريب هنا).
5.  **تطبيق المعالجة:** تم استخدام `ColumnTransformer` و `Pipeline` من مكتبة scikit-learn لتطبيق خطوات المعالجة المذكورة أعلاه بشكل منظم على مجموعة البيانات بأكملها (باستثناء العمود المستهدف).
6.  **حفظ أدوات المعالجة:** تم حفظ كائنات `scaler` و `encoder` المجهزة وقائمة أسماء الأعمدة المعالجة باستخدام `joblib` في المسار `/Users/macbookair/Desktop/sp_project/gan_project_files` لاستخدامها لاحقًا في التحويل العكسي للبيانات الاصطناعية.
7.  **عزل بيانات الفئة الأقلية:** بما أن الهدف هو موازنة البيانات عن طريق توليد عينات للفئات الأقلية، قمنا بعزل البيانات التي تنتمي إلى الفئة الأقل تمثيلاً، وهي فئة 'Enrolled' (مسجل). تم تحديد هذه الفئة بناءً على تحليل عدم التوازن في الخطوة السابقة.
8.  **حفظ البيانات المعالجة:** تم حفظ البيانات المعالجة الخاصة بفئة 'Enrolled' فقط (بدون العمود المستهدف) في ملف جديد بصيغة CSV: `enrolled_preprocessed.csv`. هذا الملف سيُستخدم كمدخل لتدريب نماذج GAN في الخطوات التالية.

أصبحت البيانات الآن جاهزة للمرحلة التالية وهي بناء وتدريب نماذج GAN المختلفة.
