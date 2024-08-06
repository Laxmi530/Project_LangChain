from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import HuggingFaceTextGenInference
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import pypdf

