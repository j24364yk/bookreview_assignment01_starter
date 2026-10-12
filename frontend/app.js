"use strict";

/*
 * 課題1 frontend/app.js
 *
 * HTML / CSSはスターターとして完成版を配布しています。
 * JavaScriptのAPI通信部分は、第5回を中心に実装します。
 *
 * 最終的に実装する主な機能
 *   - Book一覧取得
 *   - Book登録
 *   - Book詳細取得
 *   - Book削除
 *   - Review登録
 *   - Review削除
 */

const API_BASE = "";

const bookForm = document.querySelector("#book-form");
const bookList = document.querySelector("#book-list");
const reloadBooksButton = document.querySelector("#reload-books");
const message = document.querySelector("#message");

const reviewPanel = document.querySelector("#review-panel");
const selectedBookTitle = document.querySelector("#selected-book-title");
const reviewForm = document.querySelector("#review-form");
const reviewList = document.querySelector("#review-list");

let selectedBookId = null;


// ------------------------------------------------------------
// 共通表示
// ------------------------------------------------------------
function showMessage(text, type = "") {
  message.textContent = text;
  message.className = "message";

  if (type) {
    message.classList.add(type);
  }
}


// ------------------------------------------------------------
// 第5回 TODO：Book API
// ------------------------------------------------------------
async function loadBooks() {
  // TODO:
  // GET /books をfetchし、Book一覧を取得する
  // 取得後に renderBooks() を呼び出す
  showMessage("Book一覧取得は第5回で実装します。");
}


async function createBook(bookData) {
  // TODO:
  // POST /books へJSONを送信してBookを登録する
  console.log("createBook TODO", bookData);
}


async function loadBookDetail(bookId) {
  // TODO:
  // GET /books/{book_id} でBook詳細とReview一覧を取得する
  console.log("loadBookDetail TODO", bookId);
}


async function deleteBook(bookId) {
  // TODO:
  // DELETE /books/{book_id} でBookを削除する
  console.log("deleteBook TODO", bookId);
}


// ------------------------------------------------------------
// 第5回 TODO：Review API
// ------------------------------------------------------------
async function createReview(bookId, reviewData) {
  // TODO:
  // POST /books/{book_id}/reviews へReviewを送信する
  console.log("createReview TODO", bookId, reviewData);
}


async function deleteReview(reviewId) {
  // TODO:
  // Review削除APIを呼び出す
  console.log("deleteReview TODO", reviewId);
}


// ------------------------------------------------------------
// 第5回 TODO：画面描画
// ------------------------------------------------------------
function renderBooks(books) {
  // TODO:
  // Book一覧をbookListへ表示する
  console.log("renderBooks TODO", books);
}


function renderReviews(reviews) {
  // TODO:
  // Review一覧をreviewListへ表示する
  console.log("renderReviews TODO", reviews);
}


// ------------------------------------------------------------
// イベント
// ------------------------------------------------------------
bookForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const bookData = {
    title: document.querySelector("#book-title").value.trim(),
    author: document.querySelector("#book-author").value.trim(),
    published_year: Number(document.querySelector("#book-year").value),
  };

  createBook(bookData);
});


reloadBooksButton.addEventListener("click", () => {
  loadBooks();
});


reviewForm.addEventListener("submit", (event) => {
  event.preventDefault();

  if (selectedBookId === null) {
    showMessage("先にBookを選択してください。", "error");
    return;
  }

  const reviewData = {
    reviewer: document.querySelector("#reviewer").value.trim(),
    comment: document.querySelector("#review-comment").value.trim(),
    rating: Number(document.querySelector("#review-rating").value),
  };

  createReview(selectedBookId, reviewData);
});


document.addEventListener("DOMContentLoaded", () => {
  showMessage(
    "第3〜4回はバックエンドを作成します。第5回でこの画面とAPIを接続します。"
  );
});
