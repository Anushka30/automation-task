function automatedReplyToRecruiters() {
  const REQUIRED_KEYWORDS = ["keyword1", "keyword2", "keyword3"];
  const SEARCH_QUERY = "from:recruiter@example.com is:unread";
  const AUTO_REPLY_MESSAGE =
    "Thank you for reaching out to me. I am currently exploring new opportunities and would be interested in discussing the role further.";

  const threads = GmailApp.search(SEARCH_QUERY);

  for (const thread of threads) {
    const messages = thread.getMessages();
    const message = messages[messages.length - 1];
    const body = message.getPlainBody().toLowerCase();

    const keywordCounts = REQUIRED_KEYWORDS.map((keyword) => {
      const keywordLowerCase = keyword.toLowerCase();
      const count = (
        body.match(new RegExp(`\\b${keywordLowerCase}\\b`, "g")) || []
      ).length;
      return { keyword: keywordLowerCase, count: count };
    });

    console.log(keywordCounts);

    const hasAllKeywords = REQUIRED_KEYWORDS.every((keyword) =>
      body.includes(keyword.toLowerCase())
    );

    if (hasAllKeywords) {
      thread.reply(AUTO_REPLY_MESSAGE);
      message.markRead();
    }
  }
}
