import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Github, Mail, FileText } from "lucide-react";

export default function Portfolio() {
    return (
        <div className="min-h-screen bg-gray-100 p-6">
            <header className="max-w-4xl mx-auto text-center py-12">
                <h1 className="text-4xl font-bold mb-2">홍길동 | 백엔드 개발자</h1>
                <p className="text-lg text-gray-600">NAVER 개발직무 지원 포트폴리오</p>
                <div className="flex justify-center mt-4 space-x-4">
                    <Button variant="outline"><Mail className="mr-2" size={16}/> 이메일</Button>
                    <Button variant="outline"><Github className="mr-2" size={16}/> GitHub</Button>
                    <Button variant="outline"><FileText className="mr-2" size={16}/> 이력서</Button>
                </div>
            </header>

            <section className="max-w-4xl mx-auto grid gap-6">
                <Card>
                    <CardContent className="p-6">
                        <h2 className="text-2xl font-semibold mb-2">01. About Me</h2>
                        <p className="text-gray-700">안녕하세요, 문제 해결을 좋아하고 확장 가능한 백엔드 시스템을 구축하는 데 관심이 많은 개발자 홍길동입니다. 대용량 트래픽 환경에서의 경험과 도전적인 문제 해결에 열정을 가지고 있습니다.</p>
                    </CardContent>
                </Card>

                <Card>
                    <CardContent className="p-6">
                        <h2 className="text-2xl font-semibold mb-2">02. Skills</h2>
                        <ul className="list-disc list-inside text-gray-700">
                            <li>Java, Spring Boot, JPA, Redis</li>
                            <li>MySQL, MongoDB, Elasticsearch</li>
                            <li>AWS (EC2, S3, RDS), Docker, GitHub Actions</li>
                            <li>REST API 설계, 대용량 데이터 처리, 테스트 코드 작성</li>
                        </ul>
                    </CardContent>
                </Card>

                <Card>
                    <CardContent className="p-6">
                        <h2 className="text-2xl font-semibold mb-2">03. Projects</h2>
                        <div className="space-y-4">
                            <div>
                                <h3 className="text-xl font-medium">Searchify – 실시간 검색어 추천 서비스</h3>
                                <p className="text-gray-700 text-sm">Elasticsearch와 Redis 기반 실시간 검색어 추천. 사용자 행동 로그 기반 키워드 랭킹 시스템 구현.</p>
                            </div>
                            <div>
                                <h3 className="text-xl font-medium">StockStream – 주식 데이터 스트리밍 플랫폼</h3>
                                <p className="text-gray-700 text-sm">WebSocket 기반 실시간 주가 정보 제공 시스템. Kafka를 활용한 메시지 브로커 아키텍처 설계.</p>
                            </div>
                        </div>
                    </CardContent>
                </Card>

                <Card>
                    <CardContent className="p-6">
                        <h2 className="text-2xl font-semibold mb-2">04. Experience</h2>
                        <p className="text-gray-700">카카오 인턴십 백엔드 개발 (2024.07 ~ 2024.12)<br/>- RESTful API 개발 및 테스트 자동화 경험<br/>- 장애 대응 프로세스 실무 경험</p>
                    </CardContent>
                </Card>

                <Card>
                    <CardContent className="p-6">
                        <h2 className="text-2xl font-semibold mb-2">05. Contact</h2>
                        <p className="text-gray-700">이메일: example@naver.com<br/>전화번호: 010-0000-0000<br/>GitHub: https://github.com/yourname</p>
                    </CardContent>
                </Card>
            </section>
        </div>
    );
}   
