from ai.product_requirement_document import prd_generator
from ai.functional_specification_document import fsd_generator
from ai.product_requirement_document.prd_generator import Requirement_Document
from utility.excel_util import create_prd, create_fsd
from ai.utils import extract_json_from_response
import json

import re


if __name__ == "__main__":
  data = prd_generator.generate_document()
  fsd = fsd_generator.generate_document(data)
  

  create_prd(data)
  create_fsd(fsd)
  # crew_prd_gen()
  


