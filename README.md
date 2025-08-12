# Journal-article-classifier-model
A data mining project build by 5 students from the University of zambia that preprocesses text by cleaning and tokenizing it, extracting features  from text such as word counts or TF-IDF values, train a model using machine learning algorithms on labeled data and predict the discipline of new or unseen journal articles of new or unseen journal articles by applying the trained model to their titles and abstracts, assigning the most probable discipline label


1.Business Understanding
The Journal of Law and Social Sciences publishes articles spanning multiple disciplines (for example, criminal law, constitutional law, sociology of law, public policy, criminology, legal theory, etc.). Categorization is currently manual and inconsistent, which makes search, browsing, and content recommendation inefficient. This project will develop an automatic text classification system that predicts an article’s discipline from its title and abstract, improving discoverability and reducing editorial effort.

1.2 Business Objectives
Primary objectives:

Automate classification of journal articles into discipline categories to speed up editorial workflows and enhance content discovery.

Success at this stage means producing a prototype that demonstrates that article titles and abstracts can be used to predict the correct discipline with a level of accuracy 75% ,but may be improved after further iterations. The exact performance threshold will be confirmed once more requirements are clarified.

1.3 Data Mining Goals Build an initial supervised classification model that can assign one of the predefined disciplines to a given journal article, using only its title and abstract as input features.

Document and evaluate preprocessing and modeling choices to ensure results are reproducible and explainable.

These goals may be adjusted once the available data is fully understood.

1.4 Initial Success Criteria Given that this is an early-stage CRISP-DM Business Understanding phase:

Initial Iteration: The model should demonstrate and show clear potential for improvement. As an initial target, an accuracy of ≥ 70% would indicate feasibility.

Long-term Success: Once project requirements are fully defined, the target metrics will be refined to match editorial expectations e.g 85% accuracy

Success will also be measured by stakeholder feedback on the interpretability of the results and the usefulness of the proposed classification output.

1.5 Assumptions and Risks

We assume access to a labeled dataset of articles (titles, abstracts, and discipline labels).

The number of examples per class and the class distribution are unknown and could affect model choice.

Labels may be subjective, leading to some overlap between disciplines.

Limited labeled data could require manual labeling to expand the dataset before modeling.

1.6 Next Steps

1.Confirm scope and requirements with my team members 2.Assess data availability 3.confirm the size 4.quality 5.completeness of the dataset. 6.Proceed to Data Understanding phase 6.1 perform exploratory data analysis to examine class balance, text length, and potential preprocessing needs.
