Article Classifier Model For The Journal Of Law And Social Sciences(JLSS)

The A data mining project built by 5 Software engineering students from the University of zambia that takes in article title and article abstract as input  to predict the discipline(output) from which the article belongs to in the Journal of Law and Social Sciences (JLSS). The Project is Implemented in reference to the CRSIP-DM methodology that comprises of Six(6) phases which are Business Understanding, Data Understanding, Data preparation, Modeling, Evaluation and Deployment. On each phase of the methodology, necessary steps have been implemented to make the article classifier model work which are demonstrated in the google colab book and documented in this readME file

Here's a link to our notebook: https://colab.research.google.com/drive/1buSf5TT9KbDICSrGmvXsFq_adKhiQZFj?usp=sharing


HOW TO RUN THE ARTICLE CLASSIFIER MODEL

1. Clone the repository
2. Install PYTHON, FLASK (a lightweight framework for python that lets you build fast servers), FITS[pyMupdf]( a library that extracts text from PDF), and JOBLIB(a library that allows you to save python objects into a pickle file), REQUESTS(a library that allows to handle HTTP requests) and JSONIFY( a library that allows one to convert python dictionaries to JSON responses).
3. (OPTIONAL but essential) Ensure that the pickle files, "naive_bayes_model.pkl" and "tfidf_vectorizer.pkl", are copied into the main directory for the flask application to run.
4. In  the main directory of the Project, Run the following command in CLI: "python classifier_model.py"
5. After running the command, Copy the HTTP link that will be rendered in CMD and paste it in the browser of your choice. The GUI of the article classifier model will be displayed and one can be able to add a PDF as input( an article with both TITLE and ARTICLE which are inputs it takes in) and when the "predict" button is clicked, the discipline of the article is predicted alongside the confidence level of that prediction.








