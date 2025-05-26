## الخطوة 4: تدريب نماذج التصنيف

في هذه الخطوة، قمنا بتدريب نموذجين للتصنيف (Random Forest و MLP Neural Network) على مجموعتي البيانات: المجموعة الأصلية غير المتوازنة والمجموعة المتوازنة التي تم إنشاؤها باستخدام Vanilla GAN.

### الخطوات:

1. **تحميل مجموعات البيانات المعالجة:**
   * تم تحميل مجموعات التدريب والاختبار المعالجة لكل من المجموعتين.
   * حجم مجموعة التدريب الأصلية: (3539, 36)
   * حجم مجموعة الاختبار الأصلية: (885, 36)
   * حجم مجموعة التدريب المتوازنة: (4671, 36)
   * حجم مجموعة الاختبار المتوازنة: (1168, 36)

2. **معالجة القيم المفقودة (NaN):**
   * تم اكتشاف قيم مفقودة في مجموعة البيانات المتوازنة نتيجة لعملية توليد البيانات الاصطناعية.
   * تم استخدام SimpleImputer مع استراتيجية المتوسط (mean) لملء القيم المفقودة.
   * عدد القيم المفقودة قبل المعالجة: 51 في مجموعة التدريب و 13 في مجموعة الاختبار.
   * عدد القيم المفقودة بعد المعالجة: 0 في كلتا المجموعتين.

3. **تدريب وتقييم نموذج Random Forest على المجموعة الأصلية غير المتوازنة:**
   * وقت التدريب: 0.24 ثانية
   * الدقة (Accuracy): 0.7706
   * الضبط (Precision): 0.7575
   * الاستدعاء (Recall): 0.7706
   * درجة F1 (F1 Score): 0.7560
   * تقرير التصنيف:
```
              precision    recall  f1-score   support

     Dropout       0.80      0.75      0.78       284
    Enrolled       0.59      0.36      0.45       159
    Graduate       0.79      0.93      0.85       442

    accuracy                           0.77       885
   macro avg       0.73      0.68      0.69       885
weighted avg       0.76      0.77      0.76       885

```
   * مصفوفة الارتباك (Confusion Matrix):
```
Predicted →
Actual ↓    Dropout    Enrolled   Graduate  
Dropout    213        22         49        
Enrolled   39         58         62        
Graduate   13         18         411       
```

4. **تدريب وتقييم نموذج Random Forest على المجموعة المتوازنة (Vanilla GAN):**
   * وقت التدريب: 0.21 ثانية
   * الدقة (Accuracy): 0.8322
   * الضبط (Precision): 0.8360
   * الاستدعاء (Recall): 0.8322
   * درجة F1 (F1 Score): 0.8307
   * تقرير التصنيف:
```
              precision    recall  f1-score   support

     Dropout       0.83      0.75      0.79       284
    Enrolled       0.87      0.79      0.83       442
    Graduate       0.80      0.93      0.86       442

    accuracy                           0.83      1168
   macro avg       0.84      0.82      0.83      1168
weighted avg       0.84      0.83      0.83      1168

```
   * مصفوفة الارتباك (Confusion Matrix):
```
Predicted →
Actual ↓    Dropout    Enrolled   Graduate  
Dropout    212        30         42        
Enrolled   32         348        62        
Graduate   10         20         412       
```

5. **تدريب وتقييم نموذج MLP Neural Network على المجموعة الأصلية غير المتوازنة:**
   * وقت التدريب: 2.77 ثانية
   * الدقة (Accuracy): 0.7141
   * الضبط (Precision): 0.7188
   * الاستدعاء (Recall): 0.7141
   * درجة F1 (F1 Score): 0.7163
   * تقرير التصنيف:
```
              precision    recall  f1-score   support

     Dropout       0.73      0.72      0.73       284
    Enrolled       0.41      0.44      0.43       159
    Graduate       0.82      0.81      0.81       442

    accuracy                           0.71       885
   macro avg       0.65      0.66      0.66       885
weighted avg       0.72      0.71      0.72       885

```
   * مصفوفة الارتباك (Confusion Matrix):
```
Predicted →
Actual ↓    Dropout    Enrolled   Graduate  
Dropout    205        48         31        
Enrolled   42         70         47        
Graduate   33         52         357       
```

6. **تدريب وتقييم نموذج MLP Neural Network على المجموعة المتوازنة (Vanilla GAN):**
   * وقت التدريب: 3.67 ثانية
   * الدقة (Accuracy): 0.7971
   * الضبط (Precision): 0.7958
   * الاستدعاء (Recall): 0.7971
   * درجة F1 (F1 Score): 0.7956
   * تقرير التصنيف:
```
              precision    recall  f1-score   support

     Dropout       0.76      0.69      0.72       284
    Enrolled       0.80      0.79      0.79       442
    Graduate       0.81      0.87      0.84       442

    accuracy                           0.80      1168
   macro avg       0.79      0.78      0.79      1168
weighted avg       0.80      0.80      0.80      1168

```
   * مصفوفة الارتباك (Confusion Matrix):
```
Predicted →
Actual ↓    Dropout    Enrolled   Graduate  
Dropout    196        55         33        
Enrolled   38         349        55        
Graduate   23         33         386       
```

### ملخص النتائج:

| النموذج | مجموعة البيانات | الدقة (Accuracy) | الضبط (Precision) | الاستدعاء (Recall) | درجة F1 |
|---------|-----------------|-----------------|-------------------|-------------------|---------|
| Random Forest | الأصلية غير المتوازنة | 0.7706 | 0.7575 | 0.7706 | 0.7560 |
| Random Forest | المتوازنة (Vanilla GAN) | 0.8322 | 0.8360 | 0.8322 | 0.8307 |
| MLP Neural Network | الأصلية غير المتوازنة | 0.7141 | 0.7188 | 0.7141 | 0.7163 |
| MLP Neural Network | المتوازنة (Vanilla GAN) | 0.7971 | 0.7958 | 0.7971 | 0.7956 |

### الملاحظات والاستنتاجات:

1. **تأثير موازنة البيانات على أداء Random Forest:**
   * تحسن أداء نموذج Random Forest عند استخدام البيانات المتوازنة مقارنة بالبيانات الأصلية غير المتوازنة.
   * التغير في درجة F1: 0.0747

2. **تأثير موازنة البيانات على أداء MLP Neural Network:**
   * تحسن أداء نموذج MLP Neural Network عند استخدام البيانات المتوازنة مقارنة بالبيانات الأصلية غير المتوازنة.
   * التغير في درجة F1: 0.0793

3. **مقارنة بين النموذجين:**
   * النموذج الأفضل أداءً على البيانات الأصلية غير المتوازنة: Random Forest
   * النموذج الأفضل أداءً على البيانات المتوازنة: Random Forest

4. **تأثير موازنة البيانات على تصنيف الفئة الأقلية (Enrolled):**
   * في نموذج Random Forest: تحسن أداء تصنيف فئة Enrolled (F1 score)
   * في نموذج MLP Neural Network: تحسن أداء تصنيف فئة Enrolled (F1 score)

تم حفظ جميع النماذج المدربة في المجلد `/Users/macbookair/Desktop/sp_project/gan_project_files/classification_results` للاستخدام المستقبلي أو لمزيد من التحليل.
