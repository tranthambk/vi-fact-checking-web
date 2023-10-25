from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./templates")

app = FastAPI(title="Data API")

from pydantic import BaseModel


class Claim(BaseModel):
    content: str

fake_news = {
  "News": "Giàn khoan dầu khí gặp sự cố, chết người!\n\nGiàn khoan dầu khí ngoài trời Vũng Tàu gặp sự cố, làm chết nhiều người. Được biết nguyên nhân gây ra sự cố này là do gặp phải khí độc bốc lên làm nhiều người ngạt khí.",
  "ls_evidence": [
    {
      "claim_sentence": "Giàn khoan dầu khí gặp sự cố, chết người!",
      "evidence_sentence": "Giàn khoan dầu khí của Vietsovpetro ngoài khơi Vũng Tàu - Ảnh: VSP cung cấp\n\nSáng 17-4, trao đổi với Tuổi Trẻ Online, ông Nguyễn Quỳnh Lâm - tổng giám đốc Liên doanh dầu khí Việt Nga Vietsovpetro (VSP - đóng tại Vũng Tàu) - khẳng định những tin đồn về giàn khoan, giàn khai thác của VSP gặp sự cố trong mấy ngày qua là tin đồn nhảm.",
      "label": "Neutral"
    },
    {
      "claim_sentence": "Giàn khoan dầu khí gặp sự cố, chết người!",
      "evidence_sentence": "Vị này cũng khẳng định VSP có đội cứu hộ chuyên nghiệp, và việc khí độc phát sinh khi khoan hoàn toàn có thể phát hiện sớm nên không thể có chuyện bị ngạt khí độc.",
      "label": "Refutes"
    },
    {
      "claim_sentence": "Giàn khoan dầu khí gặp sự cố, chết người!",
      "evidence_sentence": "Ngày 16-4, khi nghe tin đồn giàn khoan dầu khí gặp phải khí độc bốc lên làm nhiều người ngạt khí, người có chức năng của VSP đã cho kiểm tra ở bộ phận an toàn thì không có sự cố nào xảy ra.",
      "label": "Refutes"
    },
    {
      "claim_sentence": "Giàn khoan dầu khí gặp sự cố, chết người!",
      "evidence_sentence": "Giàn khoan của ngành dầu khí ngoài khơi Vũng Tàu đang hoạt động an toàn và không có sự cố gì như tin đồn mấy ngày qua - Ảnh: VSP cung cấp\n\nCũng trong những ngày qua, có thêm tin đồn khác và cũng là sự cố của một doanh nghiệp thăm dò, khai thác dầu khí ngoài khơi Vũng Tàu.",
      "label": "Refutes"
    },
    {
      "claim_sentence": "Giàn khoan dầu khí ngoài trời Vũng Tàu gặp sự cố, làm chết nhiều người.",
      "evidence_sentence": "Giàn khoan của ngành dầu khí ngoài khơi Vũng Tàu đang hoạt động an toàn và không có sự cố gì như tin đồn mấy ngày qua - Ảnh: VSP cung cấp\n\nCũng trong những ngày qua, có thêm tin đồn khác và cũng là sự cố của một doanh nghiệp thăm dò, khai thác dầu khí ngoài khơi Vũng Tàu.",
      "label": "Refutes"
    },
    {
      "claim_sentence": "Giàn khoan dầu khí ngoài trời Vũng Tàu gặp sự cố, làm chết nhiều người.",
      "evidence_sentence": "Giàn khoan dầu khí của Vietsovpetro ngoài khơi Vũng Tàu - Ảnh: VSP cung cấp\n\nSáng 17-4, trao đổi với Tuổi Trẻ Online, ông Nguyễn Quỳnh Lâm - tổng giám đốc Liên doanh dầu khí Việt Nga Vietsovpetro (VSP - đóng tại Vũng Tàu) - khẳng định những tin đồn về giàn khoan, giàn khai thác của VSP gặp sự cố trong mấy ngày qua là tin đồn nhảm.",
      "label": "Neutral"
    },
    {
      "claim_sentence": "Giàn khoan dầu khí ngoài trời Vũng Tàu gặp sự cố, làm chết nhiều người.",
      "evidence_sentence": "Ngày 16-4, khi nghe tin đồn giàn khoan dầu khí gặp phải khí độc bốc lên làm nhiều người ngạt khí, người có chức năng của VSP đã cho kiểm tra ở bộ phận an toàn thì không có sự cố nào xảy ra.",
      "label": "Refutes"
    },
    {
      "claim_sentence": "Giàn khoan dầu khí ngoài trời Vũng Tàu gặp sự cố, làm chết nhiều người.",
      "evidence_sentence": "Theo tìm hiểu và xác minh của Tuổi Trẻ Online, thời gian qua, doanh nghiệp này không có bất cứ một hoạt động khoan hay thăm dò nào ở vùng biển Bà Rịa - Vũng Tàu.",
      "label": "Refutes"
    },
    {
      "claim_sentence": "Giàn khoan dầu khí ngoài trời Vũng Tàu gặp sự cố, làm chết nhiều người.",
      "evidence_sentence": "Vị này cũng khẳng định VSP có đội cứu hộ chuyên nghiệp, và việc khí độc phát sinh khi khoan hoàn toàn có thể phát hiện sớm nên không thể có chuyện bị ngạt khí độc.",
      "label": "Refutes"
    },
    {
      "claim_sentence": "Giàn khoan dầu khí ngoài trời Vũng Tàu gặp sự cố, làm chết nhiều người.",
      "evidence_sentence": "Trưa 17-4, trao đổi với Tuổi Trẻ Online- ông Nguyễn Tất Hoàn- phó giám đốc Công ty thăm dò và khai thác dầu khí trong nước (PVEP POC) cũng khẳng định, không có sự cố nào xảy ra như tin đồn.",
      "label": "Refutes"
    },
    {
      "claim_sentence": "Được biết nguyên nhân gây ra sự cố này là do gặp phải khí độc bốc lên làm nhiều người ngạt khí.",
      "evidence_sentence": "Ngày 16-4, khi nghe tin đồn giàn khoan dầu khí gặp phải khí độc bốc lên làm nhiều người ngạt khí, người có chức năng của VSP đã cho kiểm tra ở bộ phận an toàn thì không có sự cố nào xảy ra.",
      "label": "Refutes"
    },
    {
      "claim_sentence": "Được biết nguyên nhân gây ra sự cố này là do gặp phải khí độc bốc lên làm nhiều người ngạt khí.",
      "evidence_sentence": "Vị này cũng khẳng định VSP có đội cứu hộ chuyên nghiệp, và việc khí độc phát sinh khi khoan hoàn toàn có thể phát hiện sớm nên không thể có chuyện bị ngạt khí độc.",
      "label": "Refutes"
    }
  ],
  "final_verdict": "Refutes"
}

@app.post("/check_news/")
def check_news(claim: Claim):
    # fact_checker = FactChecker()
    # ls_evidence, final_verdict = fact_checker.predict(claim.content)
    ls_evidence, final_verdict = fake_news["ls_evidence"], fake_news["final_verdict"]
    return {
        "News": claim.content,
        "ls_evidence": ls_evidence,
        "final_verdict": final_verdict,
    }


@app.get("/", response_class=HTMLResponse)
def get_result(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
