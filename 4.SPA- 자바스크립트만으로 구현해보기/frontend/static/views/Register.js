import Template from './Template.js';

export class Register extends Template {
    constructor(){
        super();
        this.setTitle("스터디북 - 회원가입");
    }

    async getHtml(){
        return `
        <div>
        <form id="register-form" class="form">
            <div class="form-input-wrap">
                <label for="account">아이디</label>
                <input id="account" name="account" placeholder="영문 대소문자 또는 숫자를 포함한 총 4-15자리 입력">
            </div>
            <div class="form-input-wrap">
                <label for="password">비밀번호</label>
                <input id="password" name="password" type="password" placeholder="최소 8글자 이상, 특수문자1개 이상을 포함">
            </div>
            <div class="form-input-wrap">
                <label for="nickname">닉네임</label>
                <input id="nickname" name="nickname" placeholder="이름 또는 닉네임을 입력해주세요">
            </div>
            <div class="form-input-wrap">
                <label for="email">이메일</label>
                <input id="email" name="email" placeholder="시용가능한 email을 입력해주세요">
            </div>
            <br>
            <span class="message-span"></span>
            <button type="submit">회원가입</button>
            <br>
            <span>
                이미 계정을 가지고 계신가요? 바로 <a data-href="/login" data-link class="form-info-text">로그인</a> 하세요.
            </span>
        </form>
        `;
    }
} 