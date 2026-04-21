#!/usr/bin/env node
/**
 * 小红书轮播图自动截图脚本 - 第 08 篇 模板与规范
 * 使用 Puppeteer 截取 HTML 中的卡片并保存为图片
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const OUTPUT_DIR = path.join(__dirname, '..', '..', 'assets', 'carousels', '08-templates');
const HTML_FILE = path.join(__dirname, '..', 'templates', 'xiaohongshu-canvas-08.html');

if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

async function screenshot() {
    console.log('🚀 启动浏览器...');

    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const page = await browser.newPage();
    await page.setViewport({ width: 1080, height: 1440 });

    let htmlContent = fs.readFileSync(HTML_FILE, 'utf-8');

    // 隐藏下载按钮
    htmlContent = htmlContent.replace(
        '<button class="download-btn"',
        '<button class="download-btn" style="display: none;"'
    );

    await page.setContent(htmlContent, { waitUntil: 'networkidle0' });
    await new Promise(r => setTimeout(r, 2000));

    const cards = [
        { id: 'p1', name: '01-cover.png', desc: '封面' },
        { id: 'p2', name: '02-pain.png', desc: '痛点' },
        { id: 'p3', name: '03-insight.png', desc: '核心洞察' },
        { id: 'p4', name: '04-compare.png', desc: '模板vs规范' },
        { id: 'p5', name: '05-templates.png', desc: '模板体系' },
        { id: 'p6', name: '06-rules.png', desc: '规范体系' },
        { id: 'p7', name: '07-myth.png', desc: '误区' },
        { id: 'p8', name: '08-core.png', desc: '核心观点' },
        { id: 'p9', name: '09-engage.png', desc: '互动页' }
    ];

    // 删除旧的 p1-p9.png 文件
    for (let i = 1; i <= 9; i++) {
        const oldFile = path.join(OUTPUT_DIR, `p${i}.png`);
        if (fs.existsSync(oldFile)) {
            fs.unlinkSync(oldFile);
            console.log(`🗑️  删除旧文件：p${i}.png`);
        }
    }

    for (const card of cards) {
        console.log(`📸 正在截取 ${card.desc} (${card.name})...`);

        const element = await page.$(`#${card.id}`);
        if (element) {
            await element.screenshot({
                path: path.join(OUTPUT_DIR, card.name),
                type: 'png'
            });
            console.log(`   ✅ 已保存：${path.join(OUTPUT_DIR, card.name)}`);
        } else {
            console.log(`   ❌ 未找到元素：#${card.id}`);
        }

        await page.evaluate((id) => {
            const el = document.getElementById(id);
            if (el) el.scrollIntoView({ behavior: 'smooth' });
        }, card.id);
        await new Promise(r => setTimeout(r, 500));
    }

    await browser.close();
    console.log('\n✨ 全部截图完成！');
    console.log(`📁 输出目录：${OUTPUT_DIR}`);
}

screenshot().catch(console.error);
